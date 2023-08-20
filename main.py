from switch.switch import Switch
from host.host import Host
# from controller.controller import Controller


def main():
    """
    The main function to demonstrate the simulation of switches and hosts.

    This function creates instances of the Switch and Host classes, simulating a simple network environment.

    """
    # Create instances of switches and hosts
    switch1 = Switch("Switch1")
    host1 = Host("Host1")
    host2 = Host("Host2")

    # Simulate sending a packet from host1 to host2
    packet = {'src_mac': host1.mac_address, 'dst_mac': host2.mac_address, 'msg_data': 'Hello, Host2!'}
    switch1.send_packet(packet, host2.connected_port)

    # Print host2's received packets
    host2.print_received_packets()


if __name__ == "__main__":
    main()
