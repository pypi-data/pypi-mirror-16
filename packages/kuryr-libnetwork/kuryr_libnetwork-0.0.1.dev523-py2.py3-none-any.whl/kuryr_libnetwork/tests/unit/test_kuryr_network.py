# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ddt import data
from ddt import ddt
from neutronclient.common import exceptions
from oslo_serialization import jsonutils

from kuryr_libnetwork import app
from kuryr_libnetwork.common import constants as const
from kuryr_libnetwork.tests.unit import base
from kuryr_libnetwork import utils


class TestKuryrNetworkCreateFailures(base.TestKuryrFailures):
    """Unittests for the failures for creating networks.

    This test covers error responses listed in the spec:
      http://developer.openstack.org/api-ref-networking-v2-ext.html#createProviderNetwork  # noqa
    """

    def _create_network_with_exception(self, network_name, ex):
        self.mox.StubOutWithMock(app.neutron, "create_network")
        fake_request = {
            "network": {
                "name": utils.make_net_name(network_name),
                "admin_state_up": True
            }
        }
        app.neutron.create_network(fake_request).AndRaise(ex)
        self.mox.ReplayAll()

    def _invoke_create_request(self, network_name):
        network_request = {
            'NetworkID': network_name,
            'IPv4Data': [{
                'AddressSpace': 'foo',
                'Pool': '192.168.42.0/24',
                'Gateway': '192.168.42.1/24',
                'AuxAddresses': {}
            }],
            'IPv6Data': [{
                'AddressSpace': 'bar',
                'Pool': 'fe80::/64',
                'Gateway': 'fe80::f816:3eff:fe20:57c3/64',
                'AuxAddresses': {}
            }],
            'Options': {}
        }
        response = self.app.post('/NetworkDriver.CreateNetwork',
                                 content_type='application/json',
                                 data=jsonutils.dumps(network_request))
        return response

    def test_create_network_unauthorized(self):
        docker_network_id = utils.get_hash()
        self._create_network_with_exception(
            docker_network_id, exceptions.Unauthorized())

        response = self._invoke_create_request(docker_network_id)

        self.assertEqual(401, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        self.assertEqual(
            {'Err': exceptions.Unauthorized.message}, decoded_json)

    def test_create_network_bad_request(self):
        invalid_docker_network_id = 'id-should-be-hexdigits'
        response = self._invoke_create_request(invalid_docker_network_id)

        self.assertEqual(400, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        # TODO(tfukushima): Add the better error message validation.
        self.assertIn(invalid_docker_network_id, decoded_json['Err'])
        self.assertIn('NetworkID', decoded_json['Err'])


@ddt
class TestKuryrNetworkDeleteFailures(base.TestKuryrFailures):
    """Unittests for the failures for deleting networks.

    This test covers error responses listed in the spec:
      http://developer.openstack.org/api-ref-networking-v2-ext.html#deleteProviderNetwork  # noqa
    """
    def _delete_network_with_exception(self, network_id, ex):
        fake_neutron_network_id = "4e8e5957-649f-477b-9e5b-f1f75b21c03c"
        no_networks_response = {
            "networks": []
        }
        if ex == exceptions.NotFound:
            fake_networks_response = no_networks_response
        else:
            fake_networks_response = {
                "networks": [{
                    "status": "ACTIVE",
                    "subnets": [],
                    "name": network_id,
                    "admin_state_up": True,
                    "tenant_id": "9bacb3c5d39d41a79512987f338cf177",
                    "router:external": False,
                    "segments": [],
                    "shared": False,
                    "id": fake_neutron_network_id
                }]
            }
        self.mox.StubOutWithMock(app.neutron, 'list_networks')
        t = utils.make_net_tags(network_id)
        te = t + ',' + const.KURYR_EXISTING_NEUTRON_NET
        app.neutron.list_networks(tags=te).AndReturn(no_networks_response)
        app.neutron.list_networks(tags=t).AndReturn(fake_networks_response)
        subnet_v4_id = "9436e561-47bf-436a-b1f1-fe23a926e031"
        subnet_v6_id = "64dd4a98-3d7a-4bfd-acf4-91137a8d2f51"

        docker_network_id = utils.get_hash()
        docker_endpoint_id = utils.get_hash()

        fake_v4_subnet = self._get_fake_v4_subnet(
            docker_network_id, docker_endpoint_id, subnet_v4_id)
        fake_v6_subnet = self._get_fake_v6_subnet(
            docker_network_id, docker_endpoint_id, subnet_v6_id)
        fake_subnets_response = {
            "subnets": [
                fake_v4_subnet['subnet'],
                fake_v6_subnet['subnet']
            ]
        }

        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(network_id=fake_neutron_network_id).AndReturn(
            fake_subnets_response)

        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_subnetpools_response = {"subnetpools": []}
        app.neutron.list_subnetpools(name='kuryr').AndReturn(
            fake_subnetpools_response)
        app.neutron.list_subnetpools(name='kuryr6').AndReturn(
            fake_subnetpools_response)

        self.mox.StubOutWithMock(app.neutron, 'delete_subnet')
        app.neutron.delete_subnet(subnet_v4_id).AndReturn(None)
        app.neutron.delete_subnet(subnet_v6_id).AndReturn(None)

        self.mox.StubOutWithMock(app.neutron, 'delete_network')
        app.neutron.delete_network(fake_neutron_network_id).AndRaise(ex)
        self.mox.ReplayAll()

    def _delete_network_with_subnet_exception(self, network_id, ex):
        fake_neutron_network_id = "4e8e5957-649f-477b-9e5b-f1f75b21c03c"
        no_networks_response = {
            "networks": []
        }
        fake_networks_response = {
            "networks": [{
                "status": "ACTIVE",
                "subnets": [],
                "name": network_id,
                "admin_state_up": True,
                "tenant_id": "9bacb3c5d39d41a79512987f338cf177",
                "router:external": False,
                "segments": [],
                "shared": False,
                "id": fake_neutron_network_id
            }]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_networks')
        t = utils.make_net_tags(network_id)
        te = t + ',' + const.KURYR_EXISTING_NEUTRON_NET
        app.neutron.list_networks(tags=te).AndReturn(no_networks_response)
        app.neutron.list_networks(tags=t).AndReturn(fake_networks_response)
        subnet_v4_id = "9436e561-47bf-436a-b1f1-fe23a926e031"
        subnet_v6_id = "64dd4a98-3d7a-4bfd-acf4-91137a8d2f51"

        docker_network_id = utils.get_hash()
        docker_endpoint_id = utils.get_hash()

        fake_v4_subnet = self._get_fake_v4_subnet(
            docker_network_id, docker_endpoint_id, subnet_v4_id)
        fake_v6_subnet = self._get_fake_v6_subnet(
            docker_network_id, docker_endpoint_id, subnet_v6_id)
        fake_subnets_response = {
            "subnets": [
                fake_v4_subnet['subnet'],
                fake_v6_subnet['subnet']
            ]
        }

        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(network_id=fake_neutron_network_id).AndReturn(
            fake_subnets_response)

        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_subnetpools_response = {"subnetpools": []}
        app.neutron.list_subnetpools(name='kuryr').AndReturn(
            fake_subnetpools_response)
        app.neutron.list_subnetpools(name='kuryr6').AndReturn(
            fake_subnetpools_response)

        self.mox.StubOutWithMock(app.neutron, 'delete_subnet')
        app.neutron.delete_subnet(subnet_v4_id).AndRaise(ex)
        self.mox.ReplayAll()

    def _invoke_delete_request(self, network_name):
        data = {'NetworkID': network_name}
        response = self.app.post('/NetworkDriver.DeleteNetwork',
                                 content_type='application/json',
                                 data=jsonutils.dumps(data))
        return response

    @data(exceptions.Unauthorized, exceptions.NotFound, exceptions.Conflict)
    def test_delete_network_failures(self, GivenException):
        docker_network_id = utils.get_hash()
        self._delete_network_with_exception(
            docker_network_id, GivenException())

        response = self._invoke_delete_request(docker_network_id)

        self.assertEqual(GivenException.status_code, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        self.assertEqual({'Err': GivenException.message}, decoded_json)

    def test_delete_network_bad_request(self):
        invalid_docker_network_id = 'invalid-network-id'

        response = self._invoke_delete_request(invalid_docker_network_id)

        self.assertEqual(400, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        self.assertIn(invalid_docker_network_id, decoded_json['Err'])
        self.assertIn('NetworkID', decoded_json['Err'])

    @data(exceptions.Unauthorized, exceptions.NotFound, exceptions.Conflict)
    def test_delete_network_with_subnet_deletion_failures(self,
            GivenException):
        docker_network_id = utils.get_hash()
        self._delete_network_with_subnet_exception(
            docker_network_id, GivenException())

        response = self._invoke_delete_request(docker_network_id)

        self.assertEqual(GivenException.status_code, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        self.assertEqual({'Err': GivenException.message}, decoded_json)
