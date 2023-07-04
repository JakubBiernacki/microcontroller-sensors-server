from time import sleep
from _thread import start_new_thread
import json

class DeviceDataTransmitter:
    def __init__(self, connection, devices, interval=5):
        self.interval = interval
        self.devices = devices
        self.connection = connection

        self.last_sent_data = None

        start_new_thread(self.start_transmitter, ())

    def start_transmitter(self):
        while True:
            while not self.connection.is_ready:
                pass

            self._send_data()
            sleep(self.interval)

    def _send_data(self):

        data = self.devices.get_all_data()
        jsonData = json.dumps(data)
        self.connection.send(jsonData)

        # updated_data = self.get_updated_data(data)
        #
        # if updated_data:
        #     self.connection.send(updated_data)
        #
        # self.last_sent_data = data

    def get_updated_data(self, data):
        if not self.last_sent_data:
            return data

        updated_data = {}

        for k, v in data.items():
            if v != self.last_sent_data[k]:
                updated_data[k] = v

        return updated_data
