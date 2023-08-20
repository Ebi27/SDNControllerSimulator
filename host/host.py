from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether

import random


class Host:
    def __init__(self, name):
        """
        Initialize a Host instance.

        Args:
            name (str): The name of the host.
        """
        self.name = name
        self.mac_address = self.generate_mac_address()
        self.connected_port = None
        self.received_packets = []

    @staticmethod
    def generate_mac_address():
        """
        Generate a unique MAC address for the host.

        Returns:
            str: The generated MAC address.
        """

        mac = "00:00:00:{:02x}:{:02x}:{:02x}".format(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )
        return mac

    def connect_to_switch(self, switch, port):
        """
       Connect the host to a switch.

       Args:
           switch (Switch): The switch to which the host will be connected.
           port (int): The port number on the switch where the host will be connected.
       """
        self.connected_port = port
        switch.register_host(self, port)

    @staticmethod
    def send_packet_to_switch(packet_data, switch):
        """
       Send a packet to the connected switch.

       Args:
           packet_data (dict): Dictionary containing keys 'src_mac', 'dst_mac', and 'msg_data'.
           switch (Switch): The switch to which the packet will be sent.
       """
        eth_frame = Ether(src=packet_data['src_mac'], dst=packet_data['dst_mac'])
        ip_packet = IP(src='192.168.1.1', dst='192.168.1.2')
        tcp_segment = TCP(sport=12345, dport=80)
        payload = packet_data['msg_data']

        full_packet = eth_frame / ip_packet / tcp_segment / payload
        sendp(full_packet, iface=switch.interface)

    def send_packet_to_path(self, packet_data, path):
        """
       Send a packet to a specific host through the predefined path.

       Args:
           packet_data (dict): Dictionary containing keys 'src_mac', 'dst_mac', and 'msg_data'.
           path (list): List of switches representing the predefined path.
       """
        if path:
            next_switch = path.pop(0)
            packet_data['src_mac'] = self.mac_address
            packet_data['dst_mac'] = next_switch.get_mac_address()
            self.send_packet_to_switch(packet_data, next_switch)

    def receive_packet(self, packet_data):
        """
        Receive a packet and add it to the list of received packets.

        Args:
            packet_data (dict): The received packet.
        """
        self.received_packets.append(packet_data)

    def print_received_packets(self):
        """
        Print the list of received packets.
        """
        print(f"Received packets at Host {self.name}:")
        for idx, packet_data in enumerate(self.received_packets, start=1):
            print(f"Packet {idx}: {packet_data}")
