class InputDevices:

    def __init__(self):
        self._data = []

    def add_device(self, device):
        self._data.append(device)

    def listen_all(self):
        for device in self._data:
            device.listen()

    def wait_until_all_ready(self):

        ready = False
        while not ready:
            ready = all((device.is_ready for device in self._data))
