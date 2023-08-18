
class Switch:
    def __init__(self, switch_id):
        self.switch_id = switch_id
        self.mac_table = {}  # A dictionary to store MAC addresses and associated ports
