import socket


class Host:
    """
    A simulated smart device (host) that can send and receive messages.

    Attributes:
        mac_address (str): The MAC address of the host.
        received_messages (list): A list to store received messages.

    Methods:
        send_message(message, destination_device)
            Sends a message to the specified destination device.

        receive_message(message)
            Receives a message and adds it to the list of received messages.

        print_received_messages()
            Prints the list of received messages.
    """

    def __init__(self, mac_address, src_host):
        """
        Initializes a new Host instance.

        Args:
            mac_address (str): The MAC address of the host.
        """
        self.mac_address = mac_address
        self.src_host = src_host
        self.received_messages = []

    def send_message(self, message, destination_device):
        """
        Sends a message to the specified destination device.

        Args:
            message (str): The message to send.
            destination_device (Host): The destination host to send the message to.
        """
        packet = {
            'src_mac': self.mac_address,
            'dst_mac': destination_device.mac_address,
            'msg_data': message
        }
        destination_device.receive_message(packet)

    def receive_message(self, packet):
        """
        Receives a message and adds it to the list of received messages.

        Args:
            packet (dict): The received packet containing message data.
        """
        message = packet['msg_data']
        self.received_messages.append(message)

    def print_received_messages(self):
        """Prints the list of received messages."""
        print(f"Received messages for Host {self.mac_address}:")
        for message in self.received_messages:
            print(f" - {message}")
