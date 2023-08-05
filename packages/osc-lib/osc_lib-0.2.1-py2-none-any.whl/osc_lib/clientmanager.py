#   Copyright 2012-2013 OpenStack Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

"""Manage access to the clients, including authenticating when needed."""

import copy
import logging
import sys

from oslo_utils import strutils
import requests
import six

from osc_lib.api import auth
from osc_lib import exceptions
from osc_lib import session as osc_session


LOG = logging.getLogger(__name__)

PLUGIN_MODULES = []

USER_AGENT = 'osc-lib'


class ClientCache(object):
    """Descriptor class for caching created client handles."""

    def __init__(self, factory):
        self.factory = factory
        self._handle = None

    def __get__(self, instance, owner):
        # Tell the ClientManager to login to keystone
        if self._handle is None:
            try:
                self._handle = self.factory(instance)
            except AttributeError as err:
                # Make sure the failure propagates. Otherwise, the plugin just
                # quietly isn't there.
                new_err = exceptions.PluginAttributeError(err)
                six.reraise(new_err.__class__, new_err, sys.exc_info()[2])
        return self._handle


class ClientManager(object):
    """Manages access to API clients, including authentication."""

    def __getattr__(self, name):
        # this is for the auth-related parameters.
        if name in ['_' + o.replace('-', '_')
                    for o in auth.OPTIONS_LIST]:
            return self._auth_params[name[1:]]

        raise AttributeError(name)

    def __init__(
        self,
        cli_options=None,
        api_version=None,
        pw_func=None,
    ):
        """Set up a ClientManager

        :param cli_options:
            Options collected from the command-line, environment, or wherever
        :param api_version:
            Dict of API versions: key is API name, value is the version
        :param pw_func:
            Callback function for asking the user for a password.  The function
            takes an optional string for the prompt ('Password: ' on None) and
            returns a string containing the password
        """

        self._cli_options = cli_options
        self._api_version = api_version
        self._pw_callback = pw_func
        self._url = self._cli_options.auth.get('url')
        self.region_name = self._cli_options.region_name
        self.interface = self._cli_options.interface

        self.timing = self._cli_options.timing

        self._auth_ref = None
        self.session = None

        # self.verify is the Requests-compatible form
        # self.cacert is the form used by the legacy client libs
        # self.insecure is not needed, use 'not self.verify'

        # NOTE(dtroyer): Per bug https://bugs.launchpad.net/bugs/1447784
        #                --insecure overrides any --os-cacert setting

        if self._cli_options.insecure:
            # Handle --insecure
            self.verify = False
            self.cacert = None
        else:
            if (self._cli_options.cacert is not None
                    and self._cli_options.cacert != ''):
                # --cacert implies --verify here
                self.verify = self._cli_options.cacert
                self.cacert = self._cli_options.cacert
            else:
                # Fall through also gets --verify
                self.verify = True
                self.cacert = None

        # Set up client certificate and key
        # NOTE(cbrandily): This converts client certificate/key to requests
        #                  cert argument: None (no client certificate), a path
        #                  to client certificate or a tuple with client
        #                  certificate/key paths.
        self.cert = self._cli_options.cert
        if self.cert and self._cli_options.key:
            self.cert = self.cert, self._cli_options.key

        # Get logging from root logger
        root_logger = logging.getLogger('')
        LOG.setLevel(root_logger.getEffectiveLevel())

        # NOTE(gyee): use this flag to indicate whether auth setup has already
        # been completed. If so, do not perform auth setup again. The reason
        # we need this flag is that we want to be able to perform auth setup
        # outside of auth_ref as auth_ref itself is a property. We can not
        # retrofit auth_ref to optionally skip scope check. Some operations
        # do not require a scoped token. In those cases, we call setup_auth
        # prior to dereferrencing auth_ref.
        self._auth_setup_completed = False

    def _set_default_scope_options(self):
        # TODO(mordred): This is a usability improvement that's broadly useful
        # We should port it back up into os-client-config.
        default_domain = self._cli_options.default_domain

        # NOTE(hieulq): If USER_DOMAIN_NAME, USER_DOMAIN_ID, PROJECT_DOMAIN_ID
        # or PROJECT_DOMAIN_NAME is present and API_VERSION is 2.0, then
        # ignore all domain related configs.
        if (self._api_version.get('identity') == '2.0' and
                self.auth_plugin_name.endswith('password')):
            domain_props = [
                'project_domain_name',
                'project_domain_id',
                'user_domain_name',
                'user_domain_id',
            ]
            for prop in domain_props:
                if self._auth_params.pop(prop, None) is not None:
                    LOG.warning("Ignoring domain related configs " +
                                prop + " because identity API version is 2.0")
            return

        # NOTE(aloga): The scope parameters below only apply to v3 and v3
        # related auth plugins, so we stop the parameter checking if v2 is
        # being used.
        if (self._api_version.get('identity') != '3' or
                self.auth_plugin_name.startswith('v2')):
            return

        # NOTE(stevemar): If PROJECT_DOMAIN_ID or PROJECT_DOMAIN_NAME is
        # present, then do not change the behaviour. Otherwise, set the
        # PROJECT_DOMAIN_ID to 'OS_DEFAULT_DOMAIN' for better usability.
        if ('project_domain_id' in self._auth_params and
                not self._auth_params.get('project_domain_id') and
                not self._auth_params.get('project_domain_name')):
            self._auth_params['project_domain_id'] = default_domain

        # NOTE(stevemar): If USER_DOMAIN_ID or USER_DOMAIN_NAME is present,
        # then do not change the behaviour. Otherwise, set the
        # USER_DOMAIN_ID to 'OS_DEFAULT_DOMAIN' for better usability.
        if ('user_domain_id' in self._auth_params and
                not self._auth_params.get('user_domain_id') and
                not self._auth_params.get('user_domain_name')):
            self._auth_params['user_domain_id'] = default_domain

    def setup_auth(self):
        """Set up authentication

        :param required_scope: indicate whether a scoped token is required

        This is deferred until authentication is actually attempted because
        it gets in the way of things that do not require auth.
        """

        if self._auth_setup_completed:
            return

        # If no auth type is named by the user, select one based on
        # the supplied options
        self.auth_plugin_name = auth.select_auth_plugin(self._cli_options)

        # Basic option checking to avoid unhelpful error messages
        auth.check_valid_authentication_options(
            self._cli_options,
            self.auth_plugin_name,
        )

        # Horrible hack alert...must handle prompt for null password if
        # password auth is requested.
        if (self.auth_plugin_name.endswith('password') and
                not self._cli_options.auth.get('password')):
            self._cli_options.auth['password'] = self._pw_callback()

        (auth_plugin, self._auth_params) = auth.build_auth_params(
            self.auth_plugin_name,
            self._cli_options,
        )

        self._set_default_scope_options()

        # For compatibility until all clients can be updated
        if 'project_name' in self._auth_params:
            self._project_name = self._auth_params['project_name']
        elif 'tenant_name' in self._auth_params:
            self._project_name = self._auth_params['tenant_name']

        LOG.info('Using auth plugin: %s', self.auth_plugin_name)
        LOG.debug('Using parameters %s',
                  strutils.mask_password(self._auth_params))
        self.auth = auth_plugin.load_from_options(**self._auth_params)
        # needed by SAML authentication
        request_session = requests.session()
        self.session = osc_session.TimingSession(
            auth=self.auth,
            session=request_session,
            verify=self.verify,
            cert=self.cert,
            user_agent=USER_AGENT,
        )

        self._auth_setup_completed = True

    def validate_scope(self):
        if self._auth_ref.project_id is not None:
            # We already have a project scope.
            return
        if self._auth_ref.domain_id is not None:
            # We already have a domain scope.
            return

        # We do not have a scoped token (and the user's default project scope
        # was not implied), so the client needs to be explicitly configured
        # with a scope.
        auth.check_valid_authorization_options(
            self._cli_options,
            self.auth_plugin_name,
        )

    @property
    def auth_ref(self):
        """Dereference will trigger an auth if it hasn't already"""
        if not self._auth_ref:
            self.setup_auth()
            LOG.debug("Get auth_ref")
            self._auth_ref = self.auth.get_auth_ref(self.session)
        return self._auth_ref

    def is_service_available(self, service_type):
        """Check if a service type is in the current Service Catalog"""

        # Trigger authentication necessary to discover endpoint
        if self.auth_ref:
            service_catalog = self.auth_ref.service_catalog
        else:
            service_catalog = None
        # Assume that the network endpoint is enabled.
        service_available = None
        if service_catalog:
            if service_type in service_catalog.get_endpoints():
                service_available = True
                LOG.debug("%s endpoint in service catalog", service_type)
            else:
                service_available = False
                LOG.debug("No %s endpoint in service catalog", service_type)
        else:
            LOG.debug("No service catalog")
        return service_available

    def get_endpoint_for_service_type(self, service_type, region_name=None,
                                      interface='public'):
        """Return the endpoint URL for the service type."""
        if not interface:
            interface = 'public'
        # See if we are using password flow auth, i.e. we have a
        # service catalog to select endpoints from
        if self.auth_ref:
            endpoint = self.auth_ref.service_catalog.url_for(
                service_type=service_type,
                region_name=region_name,
                interface=interface,
            )
        else:
            # Get the passed endpoint directly from the auth plugin
            endpoint = self.auth.get_endpoint(
                self.session,
                interface=interface,
            )
        return endpoint

    def get_configuration(self):
        return copy.deepcopy(self._cli_options.config)
