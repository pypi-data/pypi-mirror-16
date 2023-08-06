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

import ddt
from oslo_serialization import jsonutils
import uuid

from kuryr_libnetwork.common import config
from kuryr_libnetwork.common import constants as const
from kuryr_libnetwork.controllers import app
from kuryr_libnetwork.tests.unit import base
from kuryr_libnetwork import utils


FAKE_IP4_CIDR = '10.0.0.0/16'


@ddt.ddt
class TestKuryrIpam(base.TestKuryrBase):
    """Basic unit tests for libnetwork remote IPAM driver URI endpoints.

    This test class covers the following HTTP methods and URIs as described in
    the remote IPAM driver specification as below:

      https://github.com/docker/libnetwork/blob/9bf339f27e9f5c7c922036706c9bcc410899f249/docs/ipam.md  # noqa

    - POST /IpamDriver.GetDefaultAddressSpaces
    - POST /IpamDriver.RequestPool
    - POST /IpamDriver.ReleasePool
    - POST /IpamDriver.RequestAddress
    - POST /IpamDriver.ReleaseAddress
    """
    @ddt.data(
        ('/IpamDriver.GetDefaultAddressSpaces',
         {"LocalDefaultAddressSpace":
          config.CONF.local_default_address_space,
          "GlobalDefaultAddressSpace":
          config.CONF.global_default_address_space}),
        ('/IpamDriver.GetCapabilities',
         {"RequiresMACAddress": False}))
    @ddt.unpack
    def test_remote_ipam_driver_endpoint(self, endpoint, expected):
        response = self.app.post(endpoint)
        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual(expected, decoded_json)

    def test_ipam_driver_request_pool_with_user_pool(self):
        pool_name = utils.get_neutron_subnetpool_name(FAKE_IP4_CIDR)
        new_subnetpool = {
            'name': pool_name,
            'default_prefixlen': 16,
            'prefixes': [FAKE_IP4_CIDR]}

        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = pool_name
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        app.neutron.list_subnetpools(name=fake_name).AndReturn(
            {'subnetpools': []})
        fake_subnetpool_response = {
            'subnetpool': kuryr_subnetpools['subnetpools'][0]
        }

        self.mox.StubOutWithMock(app.neutron, 'create_subnetpool')
        app.neutron.create_subnetpool(
            {'subnetpool': new_subnetpool}).AndReturn(fake_subnetpool_response)

        self.mox.ReplayAll()

        fake_request = {
            'AddressSpace': '',
            'Pool': FAKE_IP4_CIDR,
            'SubPool': '',  # In the case --ip-range is not given
            'Options': {},
            'V6': False
        }
        response = self.app.post('/IpamDriver.RequestPool',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual(fake_kuryr_subnetpool_id, decoded_json['PoolID'])

    def test_ipam_driver_request_pool_with_pool_name_option(self):
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = 'fake_pool_name'
        new_subnetpool = {
            'name': fake_name,
            'default_prefixlen': 16,
            'prefixes': [FAKE_IP4_CIDR]}

        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        fake_subnetpool_response = {
            'subnetpool': kuryr_subnetpools['subnetpools'][0]
        }

        self.mox.StubOutWithMock(app.neutron, 'create_subnetpool')
        app.neutron.create_subnetpool(
            {'subnetpool': new_subnetpool}).AndReturn(fake_subnetpool_response)

        self.mox.ReplayAll()

        fake_request = {
            'AddressSpace': '',
            'Pool': FAKE_IP4_CIDR,
            'SubPool': '',  # In the case --ip-range is not given
            'Options': {'neutron.pool.name': 'fake_pool_name'},
            'V6': False
        }
        response = self.app.post('/IpamDriver.RequestPool',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual(fake_kuryr_subnetpool_id, decoded_json['PoolID'])

    def test_ipam_driver_request_pool_with_default_v6pool(self):
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = 'kuryr6'
        kuryr_subnetpools = self._get_fake_v6_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=['fe80::/64'])
        app.neutron.list_subnetpools(name=fake_name).AndReturn(
            {'subnetpools': kuryr_subnetpools['subnetpools']})

        self.mox.ReplayAll()

        fake_request = {
            'AddressSpace': '',
            'Pool': '',
            'SubPool': '',  # In the case --ip-range is not given
            'Options': {},
            'V6': True
        }
        response = self.app.post('/IpamDriver.RequestPool',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual(fake_kuryr_subnetpool_id, decoded_json['PoolID'])

    def test_ipam_driver_release_pool(self):
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        self.mox.StubOutWithMock(app.neutron, 'delete_subnetpool')
        app.neutron.delete_subnetpool(fake_kuryr_subnetpool_id).AndReturn(
            {})

        self.mox.ReplayAll()

        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id
        }
        response = self.app.post('/IpamDriver.ReleasePool',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)

    def test_ipam_driver_request_address(self):
        # faking list_subnetpools
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = utils.get_neutron_subnetpool_name(FAKE_IP4_CIDR)
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        app.neutron.list_subnetpools(id=fake_kuryr_subnetpool_id).AndReturn(
            kuryr_subnetpools)

        # faking list_subnets
        docker_endpoint_id = utils.get_hash()
        neutron_network_id = str(uuid.uuid4())
        subnet_v4_id = str(uuid.uuid4())
        fake_v4_subnet = self._get_fake_v4_subnet(
            neutron_network_id, docker_endpoint_id, subnet_v4_id,
            subnetpool_id=fake_kuryr_subnetpool_id,
            cidr=FAKE_IP4_CIDR)
        fake_subnet_response = {
            'subnets': [
                fake_v4_subnet['subnet']
            ]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(cidr=FAKE_IP4_CIDR).AndReturn(
            fake_subnet_response)

        # faking create_port
        fake_neutron_port_id = str(uuid.uuid4())
        fake_port = base.TestKuryrBase._get_fake_port(
            docker_endpoint_id, neutron_network_id,
            fake_neutron_port_id, const.PORT_STATUS_ACTIVE,
            subnet_v4_id,
            neutron_subnet_v4_address="10.0.0.5")
        port_request = {
            'name': 'kuryr-unbound-port',
            'admin_state_up': True,
            'network_id': neutron_network_id,
            'binding:host_id': utils.get_hostname(),
        }
        fixed_ips = port_request['fixed_ips'] = []
        fixed_ip = {'subnet_id': subnet_v4_id}
        fixed_ips.append(fixed_ip)
        self.mox.StubOutWithMock(app.neutron, 'create_port')
        app.neutron.create_port({'port': port_request}).AndReturn(fake_port)

        # Apply mocks
        self.mox.ReplayAll()

        # Testing container ip allocation
        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id,
            'Address': '',  # Querying for container address
            'Options': {}
        }
        response = self.app.post('/IpamDriver.RequestAddress',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual('10.0.0.5/16', decoded_json['Address'])

    @ddt.data((False), (True))
    def test_ipam_driver_request_specific_address(self, existing_port):
        requested_address = '10.0.0.5'
        # faking list_subnetpools
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = utils.get_neutron_subnetpool_name(FAKE_IP4_CIDR)
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        app.neutron.list_subnetpools(id=fake_kuryr_subnetpool_id).AndReturn(
            kuryr_subnetpools)

        # faking list_subnets
        docker_endpoint_id = utils.get_hash()
        neutron_network_id = str(uuid.uuid4())
        subnet_v4_id = str(uuid.uuid4())
        fake_v4_subnet = self._get_fake_v4_subnet(
            neutron_network_id, docker_endpoint_id, subnet_v4_id,
            subnetpool_id=fake_kuryr_subnetpool_id,
            cidr=FAKE_IP4_CIDR)
        fake_subnet_response = {
            'subnets': [
                fake_v4_subnet['subnet']
            ]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(cidr=FAKE_IP4_CIDR).AndReturn(
            fake_subnet_response)
        self.mox.StubOutWithMock(app.neutron, 'list_ports')

        # faking update_port or create_port
        fake_neutron_port_id = str(uuid.uuid4())
        fake_port = base.TestKuryrBase._get_fake_port(
            docker_endpoint_id, neutron_network_id,
            fake_neutron_port_id, const.PORT_STATUS_ACTIVE,
            subnet_v4_id,
            neutron_subnet_v4_address=requested_address)

        fixed_ip_existing = [('subnet_id=%s' % subnet_v4_id)]
        if existing_port:
            fake_existing_port = fake_port['port']
            fake_existing_port['binding:host_id'] = ''
            fake_existing_port['binding:vif_type'] = 'unbound'
            fake_ports_response = {'ports': [fake_existing_port]}
        else:
            fake_ports_response = {'ports': []}

        fixed_ip_existing.append('ip_address=%s' % requested_address)
        app.neutron.list_ports(fixed_ips=fixed_ip_existing).AndReturn(
            fake_ports_response)

        if existing_port:
            update_port = {
                'admin_state_up': True,
                'binding:host_id': utils.get_hostname(),
            }
            self.mox.StubOutWithMock(app.neutron, 'update_port')
            app.neutron.update_port(fake_neutron_port_id,
                                    {'port': update_port}).AndReturn(
                                        fake_port)
        else:
            port_request = {
                'name': 'kuryr-unbound-port',
                'admin_state_up': True,
                'network_id': neutron_network_id,
                'binding:host_id': utils.get_hostname(),
            }
            fixed_ips = port_request['fixed_ips'] = []
            fixed_ip = {'subnet_id': subnet_v4_id,
                        'ip_address': requested_address}
            fixed_ips.append(fixed_ip)
            self.mox.StubOutWithMock(app.neutron, 'create_port')
            app.neutron.create_port({'port': port_request}).AndReturn(
                fake_port)

        # Apply mocks
        self.mox.ReplayAll()

        # Testing container ip allocation
        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id,
            'Address': requested_address,
            'Options': {}
        }
        response = self.app.post('/IpamDriver.RequestAddress',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual(requested_address + '/16', decoded_json['Address'])

    def test_ipam_driver_request_address_overlapping_cidr(self):
        # faking list_subnetpools
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')

        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_kuryr_subnetpool_id2 = str(uuid.uuid4())

        fake_name = utils.get_neutron_subnetpool_name(FAKE_IP4_CIDR)
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        app.neutron.list_subnetpools(id=fake_kuryr_subnetpool_id).AndReturn(
            kuryr_subnetpools)

        # faking list_subnets
        docker_endpoint_id = utils.get_hash()

        neutron_network_id = str(uuid.uuid4())
        neutron_network_id2 = str(uuid.uuid4())

        neutron_subnet_v4_id = str(uuid.uuid4())
        neutron_subnet_v4_id2 = str(uuid.uuid4())

        fake_v4_subnet = self._get_fake_v4_subnet(
            neutron_network_id, docker_endpoint_id, neutron_subnet_v4_id,
            subnetpool_id=fake_kuryr_subnetpool_id,
            cidr=FAKE_IP4_CIDR)

        fake_v4_subnet2 = self._get_fake_v4_subnet(
            neutron_network_id2, docker_endpoint_id, neutron_subnet_v4_id2,
            subnetpool_id=fake_kuryr_subnetpool_id2,
            cidr=FAKE_IP4_CIDR)

        fake_subnet_response = {
            'subnets': [
                fake_v4_subnet2['subnet'],
                fake_v4_subnet['subnet']
            ]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(cidr=FAKE_IP4_CIDR).AndReturn(
            fake_subnet_response)
        # faking create_port
        fake_neutron_port_id = str(uuid.uuid4())
        fake_port = base.TestKuryrBase._get_fake_port(
            docker_endpoint_id, neutron_network_id,
            fake_neutron_port_id,
            neutron_subnet_v4_id=neutron_subnet_v4_id,
            neutron_subnet_v4_address="10.0.0.5")
        port_request = {
            'name': 'kuryr-unbound-port',
            'admin_state_up': True,
            'network_id': neutron_network_id,
            'binding:host_id': utils.get_hostname(),
        }
        port_request['fixed_ips'] = []
        fixed_ip = {'subnet_id': neutron_subnet_v4_id}
        port_request['fixed_ips'].append(fixed_ip)
        self.mox.StubOutWithMock(app.neutron, 'create_port')
        app.neutron.create_port({'port': port_request}).AndReturn(fake_port)

        # Apply mocks
        self.mox.ReplayAll()

        # Testing container ip allocation
        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id,
            'Address': '',  # Querying for container address
            'Options': {}
        }
        response = self.app.post('/IpamDriver.RequestAddress',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual('10.0.0.5/16', decoded_json['Address'])

    def test_ipam_driver_request_address_for_same_gateway(self):
        # faking list_subnetpools
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = utils.get_neutron_subnetpool_name(FAKE_IP4_CIDR)
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        app.neutron.list_subnetpools(id=fake_kuryr_subnetpool_id).AndReturn(
            kuryr_subnetpools)

        # faking list_subnets
        docker_endpoint_id = utils.get_hash()
        neutron_network_id = str(uuid.uuid4())
        subnet_v4_id = str(uuid.uuid4())
        fake_v4_subnet = self._get_fake_v4_subnet(
            neutron_network_id, docker_endpoint_id, subnet_v4_id,
            subnetpool_id=fake_kuryr_subnetpool_id,
            cidr=FAKE_IP4_CIDR)
        fake_v4_subnet['subnet'].update(gateway_ip='10.0.0.1')
        fake_subnet_response = {
            'subnets': [
                fake_v4_subnet['subnet']
            ]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(cidr=FAKE_IP4_CIDR).AndReturn(
            fake_subnet_response)

        # Apply mocks
        self.mox.ReplayAll()

        # Testing container ip allocation
        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id,
            'Address': '10.0.0.1',
            'Options': {
                const.REQUEST_ADDRESS_TYPE: const.NETWORK_GATEWAY_OPTIONS
            }
        }
        response = self.app.post('/IpamDriver.RequestAddress',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertEqual('10.0.0.1/16', decoded_json['Address'])

    def test_ipam_driver_request_address_for_different_gateway(self):
        # faking list_subnetpools
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = utils.get_neutron_subnetpool_name(FAKE_IP4_CIDR)
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR],
            name=fake_name)
        app.neutron.list_subnetpools(id=fake_kuryr_subnetpool_id).AndReturn(
            kuryr_subnetpools)

        # faking list_subnets
        docker_endpoint_id = utils.get_hash()
        neutron_network_id = str(uuid.uuid4())
        subnet_v4_id = str(uuid.uuid4())
        fake_v4_subnet = self._get_fake_v4_subnet(
            neutron_network_id, docker_endpoint_id, subnet_v4_id,
            subnetpool_id=fake_kuryr_subnetpool_id,
            cidr=FAKE_IP4_CIDR)
        fake_v4_subnet['subnet'].update(gateway_ip='10.0.0.1')
        fake_subnet_response = {
            'subnets': [
                fake_v4_subnet['subnet']
            ]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(cidr=FAKE_IP4_CIDR).AndReturn(
            fake_subnet_response)

        # Apply mocks
        self.mox.ReplayAll()

        # Testing container ip allocation
        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id,
            'Address': '10.0.0.5',  # Different with existed gw ip
            'Options': {
                const.REQUEST_ADDRESS_TYPE: const.NETWORK_GATEWAY_OPTIONS
            }
        }
        response = self.app.post('/IpamDriver.RequestAddress',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(500, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        err_message = ("Requested gateway {0} does not match with "
                       "gateway {1} in existed network.").format(
                       '10.0.0.5', '10.0.0.1')
        self.assertEqual({'Err': err_message}, decoded_json)

    def test_ipam_driver_release_address(self):
        # faking list_subnetpools
        self.mox.StubOutWithMock(app.neutron, 'list_subnetpools')
        fake_kuryr_subnetpool_id = str(uuid.uuid4())
        fake_name = str('-'.join(['kuryrPool', FAKE_IP4_CIDR]))
        kuryr_subnetpools = self._get_fake_v4_subnetpools(
            fake_kuryr_subnetpool_id, prefixes=[FAKE_IP4_CIDR], name=fake_name)
        app.neutron.list_subnetpools(id=fake_kuryr_subnetpool_id).AndReturn(
            kuryr_subnetpools)
        fake_ip4 = '10.0.0.5'

        # faking list_subnets
        docker_network_id = utils.get_hash()
        docker_endpoint_id = utils.get_hash()
        neutron_network_id = docker_network_id = str(uuid.uuid4())
        subnet_v4_id = str(uuid.uuid4())
        fake_v4_subnet = self._get_fake_v4_subnet(
            docker_network_id, docker_endpoint_id, subnet_v4_id,
            subnetpool_id=fake_kuryr_subnetpool_id,
            cidr=FAKE_IP4_CIDR)
        fake_subnet_response = {
            'subnets': [
                fake_v4_subnet['subnet']
            ]
        }
        self.mox.StubOutWithMock(app.neutron, 'list_subnets')
        app.neutron.list_subnets(cidr=FAKE_IP4_CIDR).AndReturn(
            fake_subnet_response)

        #faking list_ports and delete_port
        fake_neutron_port_id = str(uuid.uuid4())
        fake_port = base.TestKuryrBase._get_fake_port(
            docker_endpoint_id, neutron_network_id,
            fake_neutron_port_id, const.PORT_STATUS_ACTIVE,
            subnet_v4_id,
            neutron_subnet_v4_address=fake_ip4)
        port_request = {
                'name': 'demo-port',
                'admin_state_up': True,
                'network_id': neutron_network_id,
        }
        rel_fixed_ips = port_request['fixed_ips'] = []
        fixed_ip = {'subnet_id': subnet_v4_id}
        fixed_ip['ip_address'] = fake_ip4
        rel_fixed_ips.append(fixed_ip)
        self.mox.StubOutWithMock(app.neutron, 'list_ports')

        list_port_response = {'ports': [fake_port['port']]}
        app.neutron.list_ports().AndReturn(
            list_port_response)

        self.mox.StubOutWithMock(app.neutron, 'delete_port')
        app.neutron.delete_port(fake_port['port']['id']).AndReturn({})

        # Apply mocks
        self.mox.ReplayAll()

        fake_request = {
            'PoolID': fake_kuryr_subnetpool_id,
            'Address': fake_ip4
        }

        response = self.app.post('/IpamDriver.ReleaseAddress',
                                content_type='application/json',
                                data=jsonutils.dumps(fake_request))

        self.assertEqual(200, response.status_code)
