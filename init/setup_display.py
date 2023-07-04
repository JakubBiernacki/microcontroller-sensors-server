from display.display import Display
from collections.devices_collection import DevicesCollection


def setup_display():
    display = Display(1)

    devices = DevicesCollection()

    display.set_next_button(devices.find_one_by_id(14))
    display.set_prev_button(devices.find_one_by_id(12))

    return display