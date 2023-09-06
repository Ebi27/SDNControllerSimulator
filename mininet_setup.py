# mininet.py
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI


class HomeAutomationTopology(Topo):
    """
        Build the custom network topology.

        This method defines the network topology by creating switches, hosts, and connecting them.
    """

    def build(self):
        """
            Create and start the Mininet network.

            This function creates a Mininet network based on the defined topology and starts it.
         """

        # Create switches
        living_room_switch = self.addSwitch('s1')
        bedroom_switch = self.addSwitch('s2')

        # Create hosts
        light_bulb = self.addHost('h1', ip='192.168.1.1/24')
        thermostat = self.addHost('h2', ip='192.168.1.2/24')
        door_lock = self.addHost('h3', ip='192.168.1.3/24')

        # Connect hosts to switches
        self.addLink(light_bulb, living_room_switch)
        self.addLink(thermostat, living_room_switch)
        self.addLink(door_lock, bedroom_switch)


def create_home_automation_network(ip, port):
    """
    Create and start the Mininet network.

    This function creates a Mininet network based on the defined topology and starts it.
    """

    topo = HomeAutomationTopology()
    net = Mininet(topo=topo, switch=OVSSwitch,
                  controller=lambda name: RemoteController(name, ip=ip, port=port))
    net.start()
    return net


if __name__ == '__main__':
    setLogLevel('info')
    controller_ip = 'RYU_CONTROLLER_IP'  # It will be replaced with Ryu controller's IP address
    controller_port = 6633  # Default Ryu controller port
    network = create_home_automation_network(controller_ip, controller_port)
    # Retrieve the controller's IP address after creating the network
    controller_ip = network.controllers[0].ip
    print(f"Controller IP: {controller_ip}")
    CLI(network)
    network.stop()
