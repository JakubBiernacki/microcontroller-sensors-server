from devices.device import Device
import dht
from time import sleep
from utils.logger import Logger

logger = Logger()


class DHT11(Device):
    type = 'dht11'

    def __init__(self, pin):
        super().__init__(pin, 1)
        self.device = dht.DHT11(self.pin)

        self.temperature = None
        self.humidity = None

    def listen(self):
        self.start_listen(self.check_measure)

    def restart(self):
        self.device = dht.DHT11(self.pin)

    def check_measure(self):

        error_count = 0

        while True:
            try:
                self.device.measure()
            except OSError as err:
                self.is_ready = False
                logger.error(self, err)

                error_count += 1
                if error_count == 5:
                    logger.info(self, 'restarting...')
                    self.restart()
                    error_count = 0
                sleep(self.interval)

                continue

            self.temperature = self.device.temperature()
            self.humidity = self.device.humidity()

            if not self.is_ready:
                self.emit_is_ready()

            sleep(self.interval)

    def get_data(self):
        data = super().get_data()

        data['data'] = {
            'temperature': self.temperature,
            'humidity': self.humidity
        }

        data['type'] = self.type

        return data
