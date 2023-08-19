import socket


class Switch:
    def __init__(self, switch_id):
        self.switch_id = switch_id
        self.mac_table = {}  # Dictionary to store MAC addresses and associated ports

    def process_packet(self, packet):
        """
        packet is a dictionary with keys: src_mac, dst_mac, msg_data
        Extract source, destination, and message data from the packet
        Check if the source MAC address is already in the MAC table
        Add the source MAC address to the table
        Check if the destination MAC address is in the MAC table
        """

        src_mac, dst_mac, msg_data = packet['src_mac'], packet['dst_mac'], packet['msg_data']
        if src_mac not in self.mac_table:
            self.mac_table[src_mac] = dst_mac

        if dst_mac in self.mac_table:
            self.forward_packet(self.mac_table[dst_mac], packet)
        else:
            self.broadcast_packet(packet)

    def forward_packet(self, output_port, packet):
        """
        mac_table is a dictionary with keys: mac_address, values: output_port
        output_port is an integer from 1 to n, where n is the number of ports on the switch
        send a packet to a specific port based on the destination MAC address.
       """

        self.send_packet(packet, output_port)

    @staticmethod
    def send_packet(self, packet, output_port):
        """
        Implement the sending of the packet to the specified output port
        Use your networking library or mechanism here
        """
        destination_ip = '127.0.0.1'
        destination_port = output_port

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto(packet.encode(), (destination_ip, destination_port))
                print(f"Packet sent to port {destination_port}")
        except Exception as e:
            print(f"Error sending packet: {e}")

    def broadcast_packet(self, packet):
        """
        Implement broadcasting logic to send the packet to all connected devices
        Loop through all the ports on the switch and send the packet to all ports except the one it was received on
        when the destination MAC address is unknown or broadcast.
        """

        for port in self.mac_table.values():
            if port != packet['src_mac']:  # Avoid sending the packet back to the source
                self.send_packet(packet, port)

    def print_mac_table(self):
        print(f"MAC Table for Switch {self.switch_id}:")
        for src_mac, dst_mac in self.mac_table.items():
            print(f"MAC: {src_mac} => Port: {dst_mac}")
