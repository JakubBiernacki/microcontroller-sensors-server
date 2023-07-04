from init.setup_devices import setup_devices
from init.setup_display import setup_display
from init.setup_wifi import setup_wifi
from init.setup_server_connection import setup_server_connection
from init.setup_server import setup_server
from connections.transmitters.device_data_transmitter import DeviceDataTransmitter
from display.views.temp_view import create_temp_view
from display.views.wifi_view import create_wifi_view
from utils.logger import Logger
from utils.config import Config

logger = Logger()
config = Config('.env')


def main():
    logger.info('MAIN', 'start microcontroller')

    devices = setup_devices()
    wifi_connection = setup_wifi()
    # connection = setup_server_connection()
    # DeviceDataTransmitter(connection, devices)
    server = setup_server()
    DeviceDataTransmitter(server, devices)

    display = setup_display()
    display.add_view(create_temp_view(devices))
    display.add_view(create_wifi_view(wifi_connection))

    devices.wait_until_all_ready()

    while True:
        display.update()
        print('debug...', end='\r')


if __name__ == '__main__':
    main()
