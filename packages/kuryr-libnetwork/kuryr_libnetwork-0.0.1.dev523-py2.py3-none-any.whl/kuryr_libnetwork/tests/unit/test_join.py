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

import uuid

import ddt
from oslo_concurrency import processutils
from oslo_serialization import jsonutils
from werkzeug import exceptions as w_exceptions

from kuryr.lib import binding
from kuryr.lib import exceptions
from kuryr_libnetwork import app
from kuryr_libnetwork.common import constants as const
from kuryr_libnetwork.tests.unit import base
from kuryr_libnetwork import utils


@ddt.ddt
class TestKuryrJoinFailures(base.TestKuryrFailures):
    """Unit tests for the failures for binding a Neutron port."""
    def _invoke_join_request(self, docker_network_id,
                             docker_endpoint_id, container_id):
        data = {
            'NetworkID': docker_network_id,
            'EndpointID': docker_endpoint_id,
            'SandboxKey': utils.get_sandbox_key(container_id),
            'Options': {},
        }
        response = self.app.post('/NetworkDriver.Join',
                                 content_type='application/json',
                                 data=jsonutils.dumps(data))

        return response

    def _port_bind_with_exeption(self, docker_endpoint_id, neutron_port,
                                 neutron_subnets, ex):
        fake_ifname = 'fake-veth'
        fake_binding_response = (
            fake_ifname,
            const.CONTAINER_VETH_PREFIX + fake_ifname,
            ('fake stdout', '')
        )
        self.mox.StubOutWithMock(binding, 'port_bind')
        if ex:
            binding.port_bind(
                docker_endpoint_id, neutron_port, neutron_subnets).AndRaise(ex)
        else:
            binding.port_bind(
                docker_endpoint_id, neutron_port, neutron_subnets).AndReturn(
                fake_binding_response)
        self.mox.ReplayAll()

        return fake_binding_response

    @ddt.data(exceptions.VethCreationFailure,
              processutils.ProcessExecutionError)
    def test_join_veth_failures(self, GivenException):
        fake_docker_network_id = utils.get_hash()
        fake_docker_endpoint_id = utils.get_hash()
        fake_container_id = utils.get_hash()

        fake_neutron_network_id = str(uuid.uuid4())
        self._mock_out_network(fake_neutron_network_id, fake_docker_network_id)
        fake_neutron_port_id = str(uuid.uuid4())
        self.mox.StubOutWithMock(app.neutron, 'list_ports')
        neutron_port_name = utils.get_neutron_port_name(
            fake_docker_endpoint_id)
        fake_neutron_v4_subnet_id = str(uuid.uuid4())
        fake_neutron_v6_subnet_id = str(uuid.uuid4())
        fake_neutron_ports_response = self._get_fake_ports(
            fake_docker_endpoint_id, fake_neutron_network_id,
            fake_neutron_port_id, const.PORT_STATUS_ACTIVE,
            fake_neutron_v4_subnet_id, fake_neutron_v6_subnet_id)
        app.neutron.list_ports(name=neutron_port_name).AndReturn(
            fake_neutron_ports_response)

        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        fake_neutron_subnets_response = self._get_fake_subnets(
            fake_docker_endpoint_id, fake_neutron_network_id,
            fake_neutron_v4_subnet_id, fake_neutron_v6_subnet_id)
        app.neutron.list_subnets(network_id=fake_neutron_network_id).AndReturn(
            fake_neutron_subnets_response)
        fake_neutron_port = fake_neutron_ports_response['ports'][0]
        fake_neutron_subnets = fake_neutron_subnets_response['subnets']

        fake_message = "fake message"
        fake_exception = GivenException(fake_message)
        self._port_bind_with_exeption(
            fake_docker_endpoint_id, fake_neutron_port,
            fake_neutron_subnets, fake_exception)
        self.mox.ReplayAll()

        response = self._invoke_join_request(
            fake_docker_network_id, fake_docker_endpoint_id, fake_container_id)

        self.assertEqual(
            w_exceptions.InternalServerError.code, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        self.assertIn(fake_message, decoded_json['Err'])

    def test_join_bad_request(self):
        fake_docker_network_id = utils.get_hash()
        invalid_docker_endpoint_id = 'id-should-be-hexdigits'
        fake_container_id = utils.get_hash()

        response = self._invoke_join_request(
            fake_docker_network_id, invalid_docker_endpoint_id,
            fake_container_id)

        self.assertEqual(
            w_exceptions.BadRequest.code, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        # TODO(tfukushima): Add the better error message validation.
        self.assertIn(invalid_docker_endpoint_id, decoded_json['Err'])
        self.assertIn('EndpointID', decoded_json['Err'])
