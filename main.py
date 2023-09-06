import argparse
from switch.switch import Switch
from host.host import Host
from controller.controller import Controller


def main():
    parser = argparse.ArgumentParser(description="SDN-based home automation network simulator")
    parser.add_argument("--controller-ip", required=True, help="IP address of the controller")
    parser.add_argument("--src-host", required=True, choices=["living_room_switch", "bedroom_switch"],
                        help="Source host for flow rule definition")
    args = parser.parse_args()

    # Create switches
    living_room_switch = Switch("LS")
    bedroom_switch = Switch("BS")

    # Create smart devices (hosts)
    smart_light_bulb = Host("AA:BB:CC:01", "living_room_switch")
    smart_thermostat = Host("AA:BB:CC:02", "bedroom_switch")
    smart_door_lock = Host("AA:BB:CC:03", "bedroom_switch")

    # Determine the selected source host
    if args.src_host == "living_room_switch":
        selected_src_host = living_room_switch
    else:
        selected_src_host = bedroom_switch

    # Create the controller
    switches = [living_room_switch, bedroom_switch]
    controller = Controller(switches, args.controller_ip, 9000, selected_src_host)

    # Determine the destination device
    if args.src_host == "living_room_switch":
        destination_device = smart_light_bulb
    else:
        destination_device = smart_thermostat

    # Define flow rule
    controller.define_flow_rule(selected_src_host, destination_device)

    # Start receiving updates from switches in a separate thread
    import threading
    updates_thread = threading.Thread(target=controller.receive_updates_from_switches)
    updates_thread.start()

    print("Simulation started. Type 'exit' to quit.")

    while True:
        command = input("Enter a command ('send' or 'exit'): ")
        if command == "send":
            message = input("Enter the message: ")
            device_name = input("Enter the device name (smart_light_bulb, smart_thermostat, smart_door_lock): ")
            source_device = None
            if device_name == "smart_light_bulb":
                source_device = smart_light_bulb
            elif device_name == "smart_thermostat":
                source_device = smart_thermostat
            elif device_name == "smart_door_lock":
                source_device = smart_door_lock

            if source_device:
                destination_device = selected_src_host  # The destination is the selected source host
                source_device.send_message(message, destination_device)

        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")

    # Print received messages at each host
    smart_light_bulb.print_received_messages()
    smart_thermostat.print_received_messages()
    smart_door_lock.print_received_messages()


if __name__ == "__main__":
    main()
