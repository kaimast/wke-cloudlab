# pylint: disable=missing-module-docstring

import geni.rspec.pg as PG

def generate_topology(num_nodes, hardware_type, os_image):
    '''
    Allows to create a new configuration on cloudlab.
    You can issue it via the cloudlab API or generate and XML file from it.

    This will simply generate a star topology with n nodes and one switch.
    All nodes will be connected to that switch.
    '''

    request = PG.Request()

    lan = PG.Link("local_net")
    lan.best_effort = True
    request.addResource(lan)

    private_ips = {}

    def allocate_machine(name):
        idx = len(private_ips)
        ip_addr = f"10.1.1.{idx+1}"
        private_ips[name] = ip_addr

        machine = PG.RawPC(name)

        machine.disk_image = f"urn:publicid:IDN+utah.cloudlab.us+image+emulab-ops//{os_image}"
        machine.hardware_type = hardware_type

        intf = lan.addNode(machine)
        intf.addAddress(PG.IPv4Address(ip_addr, "255.255.255.0"))

        request.addResource(machine)

    for pos in range(num_nodes):
        allocate_machine(f"node{pos}")

    return request
