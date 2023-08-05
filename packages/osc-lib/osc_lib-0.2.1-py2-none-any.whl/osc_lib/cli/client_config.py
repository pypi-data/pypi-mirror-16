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

"""OpenStackConfig subclass for argument compatibility"""

import logging

from os_client_config.config import OpenStackConfig


LOG = logging.getLogger(__name__)


# Sublcass OpenStackConfig in order to munge config values
# before auth plugins are loaded
class OSC_Config(OpenStackConfig):

    def _auth_select_default_plugin(self, config):
        """Select a default plugin based on supplied arguments

        Migrated from auth.select_auth_plugin()
        """

        identity_version = config.get('identity_api_version', '')

        if config.get('username', None) and not config.get('auth_type', None):
            if identity_version == '3':
                config['auth_type'] = 'v3password'
            elif identity_version.startswith('2'):
                config['auth_type'] = 'v2password'
            else:
                # let keystoneauth figure it out itself
                config['auth_type'] = 'password'
        elif config.get('token', None) and not config.get('auth_type', None):
            if identity_version == '3':
                config['auth_type'] = 'v3token'
            elif identity_version.startswith('2'):
                config['auth_type'] = 'v2token'
            else:
                # let keystoneauth figure it out itself
                config['auth_type'] = 'token'
        else:
            # The ultimate default is similar to the original behaviour,
            # but this time with version discovery
            if not config.get('auth_type', None):
                config['auth_type'] = 'password'

        LOG.debug("Auth plugin %s selected" % config['auth_type'])
        return config

    def _auth_v2_arguments(self, config):
        """Set up v2-required arguments from v3 info

        Migrated from auth.build_auth_params()
        """

        if ('auth_type' in config and config['auth_type'].startswith("v2")):
            if 'project_id' in config:
                config['tenant_id'] = config['project_id']
            if 'project_name' in config:
                config['tenant_name'] = config['project_name']
        return config

    def _auth_v2_ignore_v3(self, config):
        """Remove v3 arguemnts if present for v2 plugin

        Migrated from clientmanager.setup_auth()
        """

        # NOTE(hieulq): If USER_DOMAIN_NAME, USER_DOMAIN_ID, PROJECT_DOMAIN_ID
        # or PROJECT_DOMAIN_NAME is present and API_VERSION is 2.0, then
        # ignore all domain related configs.
        if (config.get('identity_api_version', '').startswith('2') and
                config.get('auth_type', None).endswith('password')):
            domain_props = [
                'project_domain_id',
                'project_domain_name',
                'user_domain_id',
                'user_domain_name',
            ]
            for prop in domain_props:
                if config.pop(prop, None) is not None:
                    LOG.warning("Ignoring domain related config " +
                                prop + " because identity API version is 2.0")
        return config

    def _auth_default_domain(self, config):
        """Set a default domain from available arguments

        Migrated from clientmanager.setup_auth()
        """

        identity_version = config.get('identity_api_version', '')
        auth_type = config.get('auth_type', None)

        # TODO(mordred): This is a usability improvement that's broadly useful
        # We should port it back up into os-client-config.
        default_domain = config.get('default_domain', None)
        if (identity_version == '3' and
                not auth_type.startswith('v2') and
                default_domain):

            # NOTE(stevemar): If PROJECT_DOMAIN_ID or PROJECT_DOMAIN_NAME is
            # present, then do not change the behaviour. Otherwise, set the
            # PROJECT_DOMAIN_ID to 'OS_DEFAULT_DOMAIN' for better usability.
            if ('project_domain_id' in config and
                    not config.get('project_domain_id') and
                    not config.get('project_domain_name')):
                config['project_domain_id'] = default_domain

            # NOTE(stevemar): If USER_DOMAIN_ID or USER_DOMAIN_NAME is present,
            # then do not change the behaviour. Otherwise, set the
            # USER_DOMAIN_ID to 'OS_DEFAULT_DOMAIN' for better usability.
            if ('user_domain_id' in config and
                    not config.get('user_domain_id') and
                    not config.get('user_domain_name')):
                config['user_domain_id'] = default_domain
        return config

    def auth_config_hook(self, config):
        """Allow examination of config values before loading auth plugin

        OpenStackClient will override this to perform additional chacks
        on auth_type.
        """

        config = self._auth_select_default_plugin(config)
        config = self._auth_v2_arguments(config)
        config = self._auth_v2_ignore_v3(config)
        config = self._auth_default_domain(config)

        LOG.debug("auth_config_hook(): %s" % config)
        return config
