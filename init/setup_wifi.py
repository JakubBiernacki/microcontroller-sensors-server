from connections.wifi_connection import WiFiConnection
from utils.config import Config

config = Config()


def setup_wifi():
    return WiFiConnection(config.get('WIFI_SSID'), config.get('WIFI_PASSWORD'))
