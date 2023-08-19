from switch.switch import Switch
from host.host import Host

def main():
    """
    The main function to demonstrate the simulation of switches and hosts.

    This function creates instances of the Switch and Host classes, simulating a simple network environment.

    """
    # Create switches and hosts
    switch1 = Switch("Switch1")
    host1 = Host("Host1")

if __name__ == "__main__":
    """
    Entry point of the script to demonstrate the switch logic.
    
    Creates an instance of the Switch class, processes a sample packet, and prints the MAC table.
    """
    switch = Switch("Switch1")
    packet = {'src_mac': 'src_mac', 'dst_mac': 'dst_mac', 'msg_data': 'msg_data'}
    switch.process_packet(packet)
    switch.print_mac_table()
