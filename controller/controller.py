import requests
import socket
import threading
from host.host import Host
from controller.payload import install_flow_rule_payload, update_flow_rule_payload


class Controller:
    """
    A class to manage flow control and optimize energy usage in the network.

    This class represents the SDN controller responsible for optimizing communication between smart devices(hosts)
    and switches
    to conserve energy. It defines methods for installing and updating flow rules based on predefined paths.

    Attributes:
        switches (list): A list of switches in the network.
        paths (dict): A dictionary to store predefined paths for traffic optimization.

    Methods:
        install_flow_rule(source_device, destination_device)
            Install a flow rule for communication between source and destination devices using APIs.

        update_flow_rule(source_device, destination_device)
            Update an existing flow rule based on changing network conditions using APIs.

        optimize_energy_usage()
            Optimize energy usage by prioritizing communication paths that conserve energy.
            This function implements decision-making logic to update flow rules using APIs.

    """

    def __init__(self, switches, controller_ip, controller_port, src_host):
        """
        Initialize a Controller instance.

        Args:
            switches (list): A list of switches in the network.
        """
        self.switches = switches
        self.paths = {}
        self.src_host = src_host
        self.controller_ip = controller_ip
        self.controller_port = controller_port
        self.BASE_URL = "https://sdncontroller.com/api/v1"
        self.HEADERS = {"Content-Type": "application/json"}

    def start_switch_listener(self):
        """
        Start a thread to listen for updates from switches.

        This method creates a thread that listens for updates from switches using UDP.
        The thread runs the _listen_for_switch_updates method.
        """
        switch_listener = threading.Thread(target=self._listen_for_switch_updates)
        switch_listener.start()

    def _listen_for_switch_updates(self):
        """
        Listens for updates from switches.

        This method binds a socket to the controller's IP and port and listens for updates
        from switches using UDP. Received updates are printed to the console.
        """
        switch_listen_address = (self.controller_ip, self.controller_port)
        switch_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        switch_socket.bind(switch_listen_address)

        while True:
            data, switch_address = switch_socket.recvfrom(1024)
            print(f"Received update from switch at {switch_address}: {data.decode()}")

            switch_socket.close()

    def receive_updates_from_switches(self):
        """
        Receive updates from switches through a UDP socket mechanism.
        """
        controller_address = (self.controller_ip, self.controller_port)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.bind(controller_address)
                print(f"Controller is listening on {self.controller_ip}:{self.controller_port}")
                while True:
                    update_message, switch_address = sock.recvfrom(1024)
                    print(f"Received update from {switch_address}: {update_message.decode()}")
        except Exception as e:
            print(f"Error receiving updates: {e}")

    def define_flow_rule(self, source_device, destination_device, dst_mac, dst_port):
        """
        Install a flow rule for communication between source and destination devices using APIs.

        Args:
            source_device (Device): The source smart device.
            destination_device (Device): The destination smart device.
            dst_mac: The destination MAC address.
            dst_port: The destination port.

        """

        # Implement the logic to send API requests to hosts or switches
        if isinstance(source_device, Host):
            src_mac = source_device.mac_address
            src_host = source_device.src_host
        else:
            src_mac = source_device.mac_address
            src_host = source_device.switch_id

        if isinstance(destination_device, Host):
            dst_mac = destination_device.mac_address
        else:
            dst_mac = None

        # Update the payload with dynamic data for the devices
        install_flow_rule_payload["match"]["eth_src"] = src_mac
        if dst_mac is not None:
            install_flow_rule_payload["match"]["eth_dst"] = dst_mac
        if dst_port is not None:
            install_flow_rule_payload["actions"][0]["port"] = dst_port

        try:
            response = requests.post(self.BASE_URL + "/hosts/" + src_host + "/flow_rules",
                                     json=install_flow_rule_payload, headers=self.HEADERS)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the API request:", e)
        else:
            print("Flow rule installed on device " + src_host)

    def optimize_energy_usage(self):
        """
        Optimize energy usage by prioritizing communication paths that conserve energy.
        This function implements decision-making logic to update flow rules using APIs.

        The energy optimization algorithm considers factors like path length, network load,
        and priority of traffic to select the optimal flow path for each communication.

        """

        # Implement the logic to prioritize paths and update flow rules using APIs
        for source_device, destination_flow_paths in self.paths.items():
            for destination_device, flow_path in destination_flow_paths.items():
                energy_efficiency = self.calculate_energy_efficiency(flow_path)

                if energy_efficiency > flow_path["energy_efficiency"]:
                    update_flow_rule_payload(source_device, destination_device)
                    flow_path["energy_efficiency"] = energy_efficiency
                    print(f"Optimized flow rule for communication from {source_device.name} to "
                          f"{destination_device.name}")

    def calculate_energy_efficiency(self, flow_path):
        """
        Calculate the energy efficiency score for a given flow path.

        This function can consider factors like path length, network load, and priority of traffic.

        Args:
            flow_path (dict): The flow path between source and destination hosts.

        Returns:
            float: The calculated energy efficiency score.
        """
        path_length = len(flow_path["switches"]) + 1  # Including source and destination hosts
        network_load = self.calculate_network_load(flow_path["switches"])
        traffic_priority = self.determine_traffic_priority(flow_path["traffic_type"])

        # Combine factors to calculate energy efficiency score
        energy_efficiency = (1 / path_length) * (1 - network_load) * traffic_priority
        return energy_efficiency

    @staticmethod
    def calculate_network_load(switches):
        """
        Calculate the network load for a given set of switches.

        This function could be more sophisticated, considering switch capacities and current loads.

        Args:
            switches (list): List of switches in the flow path.

        Returns:
            float: The calculated network load.
        """
        return sum(switch.load for switch in switches)

    @staticmethod
    def determine_traffic_priority(traffic_type):
        """
        Determine the priority of traffic based on its type.

        Args:
            traffic_type (str): Type of traffic (e.g., "lighting", "temperature", ...).

        Returns:
            float: The priority value for the traffic type.
        """

        priority_map = {"lighting": 0.9, "temperature": 0.7, "lock_control": 0.5}
        return priority_map.get(traffic_type, 0.5)  # Default to medium priority
