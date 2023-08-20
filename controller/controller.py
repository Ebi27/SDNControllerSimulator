import requests

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

    def __init__(self, switches):
        """
        Initialize a Controller instance.

        Args:
            switches (list): A list of switches in the network.
        """
        self.switches = switches
        self.paths = {}
        self.BASE_URL = "https://sdncontroller.com/api/v1"
        self.HEADERS = {"Content-Type": "application/json"}

    def define_flow_rule(self, source_device, destination_device):
        """
        Install a flow rule for communication between source and destination devices using APIs.

        Args:
            source_device (Device): The source smart device.
            destination_device (Device): The destination smart device.
        """

        # Implement the logic to send API requests to hosts
        src_mac = source_device["src_mac"]
        dst_mac = destination_device["dst_mac"]
        src_host = source_device["src_host"]
        dst_port = destination_device["dst_port"]

        # Update the payload with dynamic data to the three smart devices
        install_flow_rule_payload["match"]["eth_src"] = src_mac
        install_flow_rule_payload["match"]["eth_dst"] = dst_mac
        install_flow_rule_payload["actions"][0]["port"] = dst_port

        try:
            response = requests.post(self.BASE_URL + "/hosts/" + src_host + "/flow_rules",
                                     json=install_flow_rule_payload, headers=self.HEADERS)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the API request:", e)
        else:
            print("Flow rule installed on switch " + src_host)

    def update_flow_rule(self, source_device, destination_device):
        """
        Update an existing flow rule based on changing network conditions using APIs.

        Args:
            source_device (Device): The source smart device.
            destination_device (Device): The destination smart device.
        """

        # Use APIs to communicate with switches and update flow rules
        # Implement the logic to send API requests to switches
        src_mac = source_device.mac_address
        dst_mac = destination_device.mac_address

        update_flow_rule_payload["match"]["eth_src"] = src_mac
        update_flow_rule_payload["match"]["eth_dst"] = dst_mac

        try:
            response = requests.post(
                f"{self.BASE_URL}/hosts/{source_device.name}/flow_rules",
                json=update_flow_rule_payload,
                headers=self.HEADERS
            )
            response.raise_for_status()
            print(f"Updated flow rule for communication from {source_device.name} to {destination_device.name}")
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the API request:", e)

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
                self.update_flow_rule(source_device, destination_device)
                flow_path["energy_efficiency"] = energy_efficiency
                print(f"Optimized flow rule for communication from {source_device.name} to {destination_device.name}")

    def calculate_energy_efficiency(self, flow_path):
        """
        Calculate the energy efficiency score for a given flow path.

        This function can consider factors like path length, network load, and priority of traffic.

        Args:
            flow_path (dict): The flow path between source and destination hosts.

        Returns:
            float: The calculated energy efficiency score.
        """


