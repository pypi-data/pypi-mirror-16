# Copyright 2016 Brocade Communications System, Inc.
# All Rights Reserved.
#
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from keystoneclient import exceptions
from oslo_config import cfg
from oslo_log import log as logging

from tacker._i18n import _LW
from tacker.agent.linux import utils as linux_utils
from tacker.common import log
from tacker.extensions import nfvo
from tacker.nfvo.drivers.vim import abstract_vim_driver
from tacker.vm import keystone


LOG = logging.getLogger(__name__)
CONF = cfg.CONF

OPTS = [cfg.StrOpt('openstack', default='/etc/tacker/vim/fernet_keys',
                   help='Dir.path to store fernet keys.')]

# same params as we used in ping monitor driver
OPENSTACK_OPTS = [
    cfg.StrOpt('count', default='1',
               help=_('number of ICMP packets to send')),
    cfg.StrOpt('timeout', default='1',
               help=_('number of seconds to wait for a response')),
    cfg.StrOpt('interval', default='1',
               help=_('number of seconds to wait between packets'))
]
cfg.CONF.register_opts(OPTS, 'vim_keys')
cfg.CONF.register_opts(OPENSTACK_OPTS, 'vim_monitor')


def config_opts():
    return [('vim_keys', OPTS), ('vim_monitor', OPENSTACK_OPTS)]


class OpenStack_Driver(abstract_vim_driver.VimAbstractDriver):
    """Driver for OpenStack VIM

    OpenStack driver handles interactions with local as well as
    remote OpenStack instances. The driver invokes keystone service for VIM
    authorization and validation. The driver is also responsible for
    discovering placement attributes such as regions, availability zones
    """

    def __init__(self):
        self.keystone = keystone.Keystone()
        self.keystone.create_key_dir(CONF.vim_keys.openstack)

    def get_type(self):
        return 'openstack'

    def get_name(self):
        return 'OpenStack VIM Driver'

    def get_description(self):
        return 'OpenStack VIM Driver'

    def authenticate_vim(self, vim_obj):
        """Validate VIM auth attributes

        Initialize keystoneclient with provided authentication attributes.
        """
        auth_url = vim_obj['auth_url']
        auth_cred = vim_obj['auth_cred']
        vim_project = vim_obj['vim_project']
        keystone_version = self._validate_auth_url(auth_url)

        if keystone_version not in auth_url:
            vim_obj['auth_url'] = auth_url + '/' + keystone_version
        if keystone_version == 'v3':
            auth_cred['project_id'] = vim_project.get('id')
            auth_cred['project_name'] = vim_project.get('name')
            if not vim_project.get('project_domain_name'):
                LOG.error(_("'project_domain_name' is missing."))
                raise nfvo.VimPorjectDomainNameMissingException()
            auth_cred['project_domain_name'] = vim_project.get(
                'project_domain_name')
            if not auth_cred.get('user_domain_name'):
                LOG.error(_("'user_domain_name' is missing."))
                raise nfvo.VimUserDomainNameMissingException()
        else:
            auth_cred['tenant_id'] = vim_project.get('id')
            auth_cred['tenant_name'] = vim_project.get('name')
            # pop stuff not supported in keystone v2
            auth_cred.pop('user_domain_name', None)
            auth_cred.pop('user_id', None)
        auth_cred['auth_url'] = vim_obj['auth_url']
        return self._initialize_keystone(keystone_version, auth_cred)

    def _validate_auth_url(self, auth_url):
        try:
            keystone_version = self.keystone.get_version(auth_url)
        except Exception as e:
            LOG.error(_('VIM Auth URL invalid'))
            raise nfvo.VimConnectionException(message=e.message)
        return keystone_version

    def _initialize_keystone(self, version, auth):
        ks_client = self.keystone.initialize_client(version=version, **auth)
        return ks_client

    def _find_regions(self, ks_client):
        if ks_client.version == 'v2.0':
            service_list = ks_client.services.list()
            heat_service_id = None
            for service in service_list:
                if service.type == 'orchestration':
                    heat_service_id = service.id
            endpoints_list = ks_client.endpoints.list()
            region_list = [endpoint.region for endpoint in
                           endpoints_list if endpoint.service_id ==
                           heat_service_id]
        else:
            region_info = ks_client.regions.list()
            region_list = [region.id for region in region_info]
        return region_list

    def discover_placement_attr(self, vim_obj, ks_client):
        """Fetch VIM placement information

        Attributes can include regions, AZ.
        """
        try:
            regions_list = self._find_regions(ks_client)
        except exceptions.Unauthorized as e:
            LOG.warning(_("Authorization failed for user"))
            raise nfvo.VimUnauthorizedException(message=e.message)
        vim_obj['placement_attr'] = {'regions': regions_list}
        return vim_obj

    @log.log
    def register_vim(self, vim_obj):
        """Validate and register VIM

        Store VIM information in Tacker for
        VNF placements
        """
        ks_client = self.authenticate_vim(vim_obj)
        self.discover_placement_attr(vim_obj, ks_client)
        self.encode_vim_auth(vim_obj['id'], vim_obj['auth_cred'])
        LOG.debug(_('VIM registration completed for %s'), vim_obj)

    @log.log
    def deregister_vim(self, vim_id):
        """Deregister VIM from NFVO

        Delete VIM keys from file system
        """
        self.delete_vim_auth(vim_id)

    @log.log
    def delete_vim_auth(self, vim_id):
        """Delete vim information

         Delete vim key stored in file system
         """
        LOG.debug(_('Attempting to delete key for vim id %s'), vim_id)
        key_file = os.path.join(CONF.vim_keys.openstack, vim_id)
        try:
            os.remove(key_file)
            LOG.debug(_('VIM key deleted successfully for vim %s'), vim_id)
        except OSError:
            LOG.warning(_('VIM key deletion unsuccessful for vim %s'), vim_id)

    @log.log
    def encode_vim_auth(self, vim_id, auth):
        """Encode VIM credentials

         Store VIM auth using fernet key encryption
         """
        fernet_key, fernet_obj = self.keystone.create_fernet_key()
        encoded_auth = fernet_obj.encrypt(auth['password'].encode('utf-8'))
        auth['password'] = encoded_auth
        key_file = os.path.join(CONF.vim_keys.openstack, vim_id)
        try:
            with open(key_file, 'w') as f:
                f.write(fernet_key.decode('utf-8'))
                LOG.debug(_('VIM auth successfully stored for vim %s'), vim_id)
        except IOError:
            raise nfvo.VimKeyNotFoundException(vim_id=vim_id)

    @log.log
    def vim_status(self, auth_url):
        """Checks the VIM health status"""
        vim_ip = auth_url.split("//")[-1].split(":")[0].split("/")[0]
        ping_cmd = ['ping',
                    '-c', cfg.CONF.vim_monitor.count,
                    '-W', cfg.CONF.vim_monitor.timeout,
                    '-i', cfg.CONF.vim_monitor.interval,
                    vim_ip]

        try:
            linux_utils.execute(ping_cmd, check_exit_code=True)
            return True
        except RuntimeError:
            LOG.warning(_LW("Cannot ping ip address: %s"), vim_ip)
            return False
