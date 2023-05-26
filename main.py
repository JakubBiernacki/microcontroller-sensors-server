from devices.dht11 import DHT11
from devices.ds18x20 import DS18X20
from devices.button import Button
from devices.display import Display


class InputDevices:
    _data = []

    def add_device(self, device):
        self._data.append(device)

    def listen_all(self):
        for device in self._data:
            device.listen()

    def wait_until_all_ready(self):

        ready = False
        while not ready:
            ready = all((device.is_ready for device in self._data))


display = Display(1)
devices = InputDevices()

temp_hum_device = DHT11(16)
devices.add_device(temp_hum_device)

temp_device = DS18X20(17)
devices.add_device(temp_device)

button = Button(14)
devices.add_device(button)


def main():
    devices.listen_all()
    devices.wait_until_all_ready()

    while True:
        display.add_row(f'tem: {temp_device.temperature:.1f} C')
        display.add_row(f'hum: {temp_hum_device.humidity} %')
        display.update()


if __name__ == '__main__':
    main()
