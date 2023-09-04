# mininet.py
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.topo import Topo
from mininet.log import setLogLevel


class MyTopology(Topo):
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
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')

        # Create hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')

        # Connect hosts to switches
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)


def create_network():
    """
    Create and start the Mininet network.

    This function creates a Mininet network based on the defined topology and starts it.
    """
    topo = MyTopology()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller)
    net.start()
    return net


if __name__ == '__main__':
    setLogLevel('info')
    network = create_network()
    network.stop()
