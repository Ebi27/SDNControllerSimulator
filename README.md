# SDN Controller Simulator

A simple Software Defined Networking (SDN) Controller Simulator project implemented in Python. Working on this project
with the aim to learn about the fundamental concepts of SDN by creating a basic controller that manages a virtual network 
of switches and hosts.

## Features

- Topology representation using Python data structures.
- Switch logic for packet forwarding based on MAC address tables.
- Host communication through switches.
- Static flow control to define fixed paths for traffic.
- Controller logic to manage flow rules in switches.
- Communication channels between switches and the controller.

## Getting Started

Follow these steps to set up and run the SDN Controller Simulator:

1. Clone this repository:

   ```
   git clone https://github.com/Ebi27/SDNControllerSimulator.git
   cd SDN-Controller-Simulator

## Run the simulator:
    python main.py
Follow the on-screen instructions to interact with the virtual network.

## Usage
- The main.py file contains the entry point for the simulator.
- The communication directory contains the communication channels between switches and controller.
- The host directory contains  Host communication and packet generation.
- The switch directory contains the switch logic and MAC address tables.
- The controller directory contains controller logic and flow control.
- Modify the code in different modules to experiment with the simulator's behavior.
- Refer to comments in the code for explanations of key functionalities.

## License
This project is licensed under the [MIT License](https://github.com/Ebi27/SDNControllerSimulator/blob/main/LICENSE).

## Acknowledgements
This project was inspired by the desire to learn and practice SDN concepts. It is not intended for production use but rather as a learning exercise.