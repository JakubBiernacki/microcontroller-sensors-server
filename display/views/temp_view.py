from devices.dht11 import DHT11
from devices.ds18x20 import DS18X20
from display.display import DisplayView


def create_temp_view(devices):
    hum_device = devices.find_one_by_type(DHT11)
    temp_device = devices.find_one_by_type(DS18X20) or hum_device

    temp_view = DisplayView('TEMP DATA')

    if temp_device:
        temp_view.add_row('temp: [%v%] C', temp_device, 'temperature')
    else:
        temp_view.add_row('temp: error')

    if hum_device:
        temp_view.add_row('hum: [%v%] %', hum_device, 'humidity')
    else:
        temp_view.add_row('hum: error')

    return temp_view
