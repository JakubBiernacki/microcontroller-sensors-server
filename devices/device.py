from machine import Pin
from _thread import start_new_thread
from utils.logger import Logger

logger = Logger()


class Device:

    def __init__(self, pin, interval=0.5):
        self._id = pin
        self.pin = Pin(pin)
        self.is_ready = False
        self.interval = interval

    def start_listen(self, func, args=()):
        logger.info(self, 'start listening')
        start_new_thread(func, args)

    def emit_is_ready(self):
        logger.info(self, 'is ready')
        self.is_ready = True

    def get_id(self):
        return self._id

    def get_data(self):
        return {'pin': self._id, 'online': self.is_ready}

    def __str__(self):
        return f'Device: {type(self).__name__} Id/Pin: {self._id}'
