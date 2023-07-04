from utils.singleton import singleton


@singleton
class DevicesCollection:

    def __init__(self, devices=None):
        if devices is None:
            devices = []
        self._data = devices

    def add_device(self, device):
        self._data.append(device)

    def listen_all(self):
        for device in self._data:
            device.listen()

    def wait_until_all_ready(self):

        ready = False
        while not ready:
            ready = all((device.is_ready for device in self._data))

    def find_all_by_type(self, device_type):
        for device in self._data:
            if isinstance(device, device_type):
                yield device

    def find_one_by_type(self, device_type):
        for device in self._data:
            if isinstance(device, device_type):
                return device
        return None

    def find_one_by_id(self, id):
        for device in self._data:
            if device.get_id() == id:
                return device
        return None

    def get_all_data(self):
        data = []

        for device in self._data:
            data.append(device.get_data())

        return data
