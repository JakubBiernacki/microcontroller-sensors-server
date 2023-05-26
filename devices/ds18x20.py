from devices.device import Device
import onewire, ds18x20
from time import sleep, sleep_ms
from _thread import start_new_thread


class DS18X20(Device):
    def __init__(self, pin):
        super().__init__(pin)

        self.ds = ds18x20.DS18X20(onewire.OneWire(self.pin))
        self.device = self.ds.scan()[0]

        self.temperature = None
        self.max_temperature = None
        self.min_temperature = None

    def listen(self):
        self.start_listen(self.check_measure)

    def check_measure(self):
        while True:
            self.ds.convert_temp()

            sleep_ms(750)

            self.temperature = self.ds.read_temp(self.device)

            self.store_temperature_data()

            if not self.is_ready:
                self.is_ready = True

            sleep(self.interval)

    def store_temperature_data(self):
        if not self.min_temperature and not self.max_temperature:
            self.min_temperature = self.temperature
            self.max_temperature = self.temperature
        else:
            if self.temperature < self.min_temperature:
                self.min_temperature = self.temperature

            elif self.temperature > self.max_temperature:
                self.max_temperature = self.temperature

    def get_data(self):
        return {
            'temperature': self.temperature,
            'max_temperature': self.max_temperature,
            'min_temperature': self.min_temperature,
        }
