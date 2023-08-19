import socket


class Switch:
    """
    A simulated network switch that processes and forwards packets based on MAC addresses.

    Attributes:
        switch_id (str): Identifier for the switch.
        mac_table (dict): A dictionary to store MAC addresses and associated ports.

    Methods:
        process_packet(packet)
            Extracts source, destination, and message data from the packet and forwards or broadcasts accordingly.

        forward_packet(output_port, packet)
            Forwards a packet to a specific output port based on the destination MAC address.

        send_packet(packet, output_port)
            Sends the packet to the specified output port using a UDP socket mechanism.

        broadcast_packet(packet)
            Sends the packet to all connected devices, excluding the source device.

        print_mac_table()
            Prints the MAC table contents for the switch.

    """

    def __init__(self, switch_id):
        """
        Initializes a new Switch instance.

        Args:
            switch_id (str): Identifier for the switch.
        """
        self.switch_id = switch_id
        self.mac_table = {}

    def process_packet(self, packet):
        """
        Processes an incoming packet and forwards or broadcasts based on MAC addresses.

        Args:
            packet (dict): Dictionary containing keys 'src_mac', 'dst_mac', and 'msg_data'.
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
        Forwards a packet to a specific output port based on the destination MAC address.

        Args:
            output_port (int): The output port number.
            packet (dict): Dictionary containing keys 'src_mac', 'dst_mac', and 'msg_data'.
        """
        self.send_packet(packet, output_port)

    @staticmethod
    def send_packet(packet, output_port):
        """
        Sends a packet to the specified output port using a UDP socket mechanism.

        Args:
            packet (dict): Dictionary containing keys 'src_mac', 'dst_mac', and 'msg_data'.
            output_port (int): The output port number.
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
        Sends the packet to all connected devices, excluding the source device.

        Args:
            packet (dict): Dictionary containing keys 'src_mac', 'dst_mac', and 'msg_data'.
        """
        for port in self.mac_table.values():
            if port != packet['src_mac']:  # Avoid sending the packet back to the source
                self.send_packet(packet, port)

    def print_mac_table(self):
        """Prints the MAC table contents for the switch."""
        print(f"MAC Table for Switch {self.switch_id}:")
        for src_mac, dst_mac in self.mac_table.items():
            print(f"MAC: {src_mac} => Port: {dst_mac}")
