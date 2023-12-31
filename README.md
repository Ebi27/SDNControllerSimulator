# SDN Controller Simulator

A simple Software Defined Networking (SDN) Controller Simulator project implemented in Python. This project aims to provide a hands-on learning experience about the fundamental concepts of SDN by creating a basic controller that manages a virtual network of switches, hosts, and integrates a trace-route tool in the context of an SDN-based home automation system.

## Scenario: SDN-Based Home Automation System with Trace-Route Integration

In this project, I am simulating an SDN-based home automation system where smart devices (hosts) are controlled by smart switches. 
The goal is to optimize energy consumption by managing the flow of data between devices. 
Additionally, I have integrated a trace-route tool as a solution from the [John Crickett's coding challenge](https://codingchallenges.fyi/challenges/challenge-traceroute) to allow 
me to trace the route of network packets for troubleshooting and monitoring purposes.

### Network Topology

- Three Smart Devices (Hosts):
   - Smart Light Bulb (MAC: AA:BB:CC:01)
   - Smart Thermostat (MAC: AA:BB:CC:02)
   - Smart Door Lock (MAC: AA:BB:CC:03)


- Two Smart Switches (Switches):
   - Living Room Switch (Switch ID: LS)
   - Bedroom Switch (Switch ID: BS)

## Features

- Topology representation using Python data structures.
- Switch logic for packet forwarding based on MAC address tables.
- Host communication through switches.
- Static flow control to define fixed paths for traffic optimization.
- Controller logic to manage flow rules and optimize energy consumption.
- Communication channels between switches and the controller.
- Integrated trace-route tool for network troubleshooting and monitoring.

## Getting Started

Follow these steps to set up and run the SDN Controller Simulator:

1. Clone this repository:

   ```
   git clone https://github.com/Ebi27/SDNControllerSimulator.git
   cd SDN-Controller-Simulator

2. Install Dependencies:

  This simulation requires Python 3 and the following modules:

    argparse: For command-line argument parsing.
    pip install scapy

## Run the simulator:
    python main.py --controller-ip <controller_ip> --src-host <src_host>

  Replace _<controller_ip>_ with the IP address of the controller and _<src_host>_ with either 'living_room_switch' or 
 _'bedroom_switch'_.

1. Follow the on-screen instructions to interact with the virtual network.

2. Type 'exit' to quit the simulation.

## Usage
- The `main.py` file contains the entry point for the simulator.
- The communication directory contains the communication channels between switches and controller.
- The host directory contains  Host communication and packet generation.
- The switch directory contains the switch logic and MAC address tables.
- The controller directory contains controller logic and flow control.
- The traceroute directory contains the trace-route tool integration.
- Modify the code in different modules to experiment with the simulator's behavior.
- Refer to comments in the code for explanations of key functionalities.

## License
This project is licensed under the [MIT License](https://github.com/Ebi27/SDNControllerSimulator/blob/main/LICENSE).

## Acknowledgements
This project was inspired by the desire to learn and practice SDN concepts. It is not intended for production use but rather as a learning exercise.