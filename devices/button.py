from devices.device import Device
from machine import Pin
from time import sleep


class Button(Device):
    type = 'button'

    def __init__(self, pin):

        super().__init__(pin, 0.2)
        self._device = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        self._last_status_is_pressed = False

        self._on_press_actions = []
        self._on_hold_actions = []
        self._on_release_actions = []

    def is_pressed(self):
        return self._device.value() == 1

    def get_data(self):

        data = super().get_data()

        data['data'] = {'is_pressed': self.is_pressed()}
        data['type'] = self.type

        return data

    def run_on_press_actions(self):
        for action in self._on_press_actions:
            action()

    def run_on_hold_actions(self):
        for action in self._on_hold_actions:
            action()

    def run_on_release_actions(self):
        for action in self._on_release_actions:
            action()

    def listen(self):
        self.start_listen(self.check_status)

    def check_status(self):
        while True:
            if self.is_pressed() and not self._last_status_is_pressed:
                self.run_on_press_actions()
            elif self.is_pressed() and self._last_status_is_pressed:
                self.run_on_hold_actions()
            elif not self.is_pressed() and self._last_status_is_pressed:
                self.run_on_release_actions()

            self._last_status_is_pressed = self.is_pressed()

            if not self.is_ready:
                self.emit_is_ready()

            sleep(self.interval)

    def on_press(self, action):
        self._on_press_actions.append(action)

    def on_hold(self, action):
        self._on_hold_actions.append(action)

    def on_release(self, action):
        self._on_release_actions.append(action)
