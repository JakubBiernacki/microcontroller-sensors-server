from machine import Pin
from _thread import start_new_thread


class Device:
    def __init__(self, pin, interval=0.5):
        self.pin = Pin(pin)
        self.interval = interval
        self.is_ready = False

    def get_data(self):
        return None

    def start_listen(self, func, args=()):
        start_new_thread(func, args)

