from collections.devices_collection import DevicesCollection
from devices.dht11 import DHT11
from devices.ds18x20 import DS18X20
from devices.button import Button


def setup_devices():
    devices = DevicesCollection()
    devices.add_device(DHT11(16))
    devices.add_device(DS18X20(17))
    devices.add_device(Button(14))
    devices.add_device(Button(12))

    devices.listen_all()

    return devices
