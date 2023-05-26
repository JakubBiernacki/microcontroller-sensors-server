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
        print(f'[Device] : {self} - start listening \n')
        start_new_thread(func, args)

    def emit_is_ready(self):
        print(f'[Device] : {self} - is ready \n')
        self.is_ready = True


