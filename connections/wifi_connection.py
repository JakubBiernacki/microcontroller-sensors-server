import network
from _thread import start_new_thread
from utils.logger import Logger

logger = Logger()


class WiFiConnection:
    def __init__(self, SSID, PASSWORD):
        self._ssid = SSID
        self._password = PASSWORD

        self.is_ready = False
        self.config = None
        self.ip = None
        start_new_thread(self._do_connect, ())

    def _do_connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            self.is_ready = False
            logger.info(self, 'connecting to network...')
            wlan.connect(self._ssid, self._password)
            while not wlan.isconnected():
                pass

        logger.info(self, 'connected')
        self.is_ready = True
        self.config = wlan.ifconfig()
        self.ip = self.config[0]
