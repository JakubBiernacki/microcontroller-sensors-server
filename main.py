from input_devices.input_devices import InputDevices
from input_devices.dht11 import DHT11
from input_devices.ds18x20 import DS18X20
from input_devices.button import Button
from output_devices.display import Display, DisplayView

devices = InputDevices()

temp_hum_device = DHT11(16)
devices.add_device(temp_hum_device)

temp_device = DS18X20(17)
devices.add_device(temp_device)

button1 = Button(14)
button2 = Button(12)
devices.add_device(button1)
devices.add_device(button2)

main_display = Display(1)
button1.on_press(main_display.next_view)
button2.on_press(main_display.prev_view)

base_view = DisplayView('ROOM DATA')
base_view.add_row('temp: [%v%] C', temp_device, 'temperature')
base_view.add_row('hum: [%v%] %', temp_hum_device, 'humidity')
main_display.add_view(base_view)

base_view = DisplayView('NEXT DATA')
base_view.add_row('temp: [%v%] C', temp_device, 'temperature')
# base_view.add_row('hum: [%v%] %', temp_hum_device, 'humidity')
main_display.add_view(base_view)

def main():
    devices.listen_all()
    devices.wait_until_all_ready()

    while True:
        main_display.update()
        print('debug...', end='\r')


if __name__ == '__main__':
    main()
