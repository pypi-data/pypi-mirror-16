# Copyright 2016 Brocade Communications System, Inc.
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

from novaclient import exceptions
from oslo_config import cfg

from tacker.tests import constants
from tacker.tests.functional import base
from tacker.tests.utils import read_file


CONF = cfg.CONF
VNF_CIRROS_CREATE_TIMEOUT = 120


class VnfTestToscaCreate(base.BaseTackerTest):
    def test_create_delete_vnf_tosca_no_monitoring(self):
        data = dict()
        data['tosca'] = read_file('sample-tosca-vnfd.yaml')
        vnfd_name = 'test_tosca_vnf_with_cirros_no_monitoring'
        toscal = data['tosca']
        tosca_arg = {'vnfd': {'name': vnfd_name,
                              'attributes': {'vnfd': toscal}}}

        # Create vnfd with tosca template
        vnfd_instance = self.client.create_vnfd(body=tosca_arg)
        self.assertIsNotNone(vnfd_instance)

        # Create vnf with vnfd_id
        vnfd_id = vnfd_instance['vnfd']['id']
        vnf_name = 'test_tosca_vnf_with_cirros_no_monitoring'
        vnf_arg = {'vnf': {'vnfd_id': vnfd_id, 'name': vnf_name}}
        vnf_instance = self.client.create_vnf(body=vnf_arg)

        self.validate_vnf_instance(vnfd_instance, vnf_instance)

        vnf_id = vnf_instance['vnf']['id']
        vnf_current_status = self.wait_until_vnf_active(
            vnf_id,
            constants.VNF_CIRROS_CREATE_TIMEOUT,
            constants.ACTIVE_SLEEP_TIME)
        self.assertEqual('ACTIVE', vnf_current_status)
        self.assertIsNotNone(self.client.show_vnf(vnf_id)['vnf']['mgmt_url'])

        # Delete vnf_instance with vnf_id
        try:
            self.client.delete_vnf(vnf_id)
        except Exception:
            assert False, "vnf Delete failed"

        # Delete vnfd_instance
        self.addCleanup(self.client.delete_vnfd, vnfd_id)
        self.addCleanup(self.wait_until_vnf_delete, vnf_id,
            constants.VNF_CIRROS_DELETE_TIMEOUT)


class VnfTestToscaCreateFlavorCreation(base.BaseTackerTest):
    def test_create_delete_vnf_tosca_no_monitoring(self):
        data = dict()
        vnfd_name = 'tosca_vnfd_with_auto_flavor'
        data['tosca'] = read_file('sample-tosca-vnfd-flavor.yaml')
        toscal = data['tosca']
        tosca_arg = {'vnfd': {'name': vnfd_name, 'attributes': {'vnfd':
                                                                toscal}}}

        # Create vnfd with tosca template
        vnfd_instance = self.client.create_vnfd(body=tosca_arg)
        self.assertIsNotNone(vnfd_instance)

        # Create vnf with vnfd_id
        vnf_name = 'tosca_vnf_with_auto_flavor'
        vnfd_id = vnfd_instance['vnfd']['id']
        vnf_arg = {'vnf': {'vnfd_id': vnfd_id, 'name': vnf_name}}
        vnf_instance = self.client.create_vnf(body=vnf_arg)

        self.validate_vnf_instance(vnfd_instance, vnf_instance)

        vnf_id = vnf_instance['vnf']['id']
        vnf_current_status = self.wait_until_vnf_active(
            vnf_id,
            constants.VNF_CIRROS_CREATE_TIMEOUT,
            constants.ACTIVE_SLEEP_TIME)
        self.assertEqual('ACTIVE', vnf_current_status)
        self.assertIsNotNone(self.client.show_vnf(vnf_id)['vnf']['mgmt_url'])

        servers = self.novaclient().servers.list()
        vdu_server = None
        for server in servers:
            if 'VDU1_flavor_func' in server.name:
                vdu_server = server
                break
        self.assertIsNotNone(vdu_server)
        flavor_id = server.flavor["id"]
        nova_flavors = self.novaclient().flavors
        flavor = nova_flavors.get(flavor_id)
        self.assertIsNotNone(flavor)
        self.assertEqual(True, "VDU1_flavor_func_flavor" in flavor.name)
        # Delete vnf_instance with vnf_id
        try:
            self.client.delete_vnf(vnf_id)
        except Exception:
            assert False, "vnf Delete failed"

        # Delete vnfd_instance
        self.addCleanup(self.client.delete_vnfd, vnfd_id)
        self.addCleanup(self.wait_until_vnf_delete, vnf_id,
            constants.VNF_CIRROS_DELETE_TIMEOUT)
        self.assertRaises(exceptions.NotFound, nova_flavors.delete,
                          [flavor_id])


class VnfTestToscaCreateImageCreation(base.BaseTackerTest):
    def test_create_delete_vnf_tosca_no_monitoring(self):
        data = dict()
        vnfd_name = 'tosca_vnfd_with_auto_image'
        data['tosca'] = read_file('sample-tosca-vnfd-image.yaml')
        toscal = data['tosca']
        tosca_arg = {'vnfd': {'name': vnfd_name, 'attributes': {'vnfd':
                                                                toscal}}}

        # Create vnfd with tosca template
        vnfd_instance = self.client.create_vnfd(body=tosca_arg)
        self.assertIsNotNone(vnfd_instance)

        # Create vnf with vnfd_id
        vnfd_id = vnfd_instance['vnfd']['id']
        vnf_name = 'tosca_vnf_with_auto_image'
        vnf_arg = {'vnf': {'vnfd_id': vnfd_id, 'name': vnf_name}}
        vnf_instance = self.client.create_vnf(body=vnf_arg)

        self.validate_vnf_instance(vnfd_instance, vnf_instance)

        vnf_id = vnf_instance['vnf']['id']
        vnf_current_status = self.wait_until_vnf_active(
            vnf_id,
            constants.VNF_CIRROS_CREATE_TIMEOUT,
            constants.ACTIVE_SLEEP_TIME)
        self.assertEqual('ACTIVE', vnf_current_status)
        self.assertIsNotNone(self.client.show_vnf(vnf_id)['vnf']['mgmt_url'])

        servers = self.novaclient().servers.list()
        vdu_server = None
        for server in servers:
            if 'VDU1_image_func' in server.name:
                vdu_server = server
                break
        self.assertIsNotNone(vdu_server)
        image_id = vdu_server.image["id"]
        nova_images = self.novaclient().images
        image = nova_images.get(image_id)
        self.assertIsNotNone(image)
        self.assertEqual(True, "VNFImage_image_func" in image.name)
        # Delete vnf_instance with vnf_id
        try:
            self.client.delete_vnf(vnf_id)
        except Exception:
            assert False, "vnf Delete failed"

        # Delete vnfd_instance
        self.addCleanup(self.client.delete_vnfd, vnfd_id)
        self.addCleanup(self.wait_until_vnf_delete, vnf_id,
            constants.VNF_CIRROS_DELETE_TIMEOUT)
        self.assertRaises(exceptions.NotFound, nova_images.delete,
                          [image_id])
