from input_devices.device import Device
import dht
from time import sleep
from _thread import start_new_thread


class DHT11(Device):
    def __init__(self, pin):
        super().__init__(pin)
        self.device = dht.DHT11(self.pin)

        self.temperature = None
        self.humidity = None

    def listen(self):
        self.start_listen(self.check_measure)

    def check_measure(self):
        while True:
            try:
                self.device.measure()
            except OSError:
                self.is_ready = False
                print(f'[Device] : {self} - error \n')
                continue

            self.temperature = self.device.temperature()
            self.humidity = self.device.humidity()

            if not self.is_ready:
                self.emit_is_ready()

            sleep(self.interval)

    def get_data(self):
        return {
            'temperature': self.temperature,
            'humidity': self.humidity
        }
