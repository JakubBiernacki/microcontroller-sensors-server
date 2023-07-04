from LIB.SH1106 import SH1106_I2C
from machine import I2C
from time import sleep


class DisplayRow:
    def __init__(self, text, obj, param):
        self.text = text
        self.object = obj
        self.param = param

    def formatted_text(self):
        if self.object and self.param:
            value = getattr(self.object, self.param)

            return self.text.replace('[%v%]', str(value))
        return self.text


class DisplayView:

    def __init__(self, name, row_height=20):
        self.name = name
        self.rows = []
        self.row_height = row_height
        self.display = None

    def add_row(self, text, obj=None, param=None):
        row = DisplayRow(text, obj, param)
        self.rows.append(row)

    def apply(self, display):
        display.text(self.name.upper(), 0, 0, 1)
        display.text('-' * len(self.name), 0, 5, 1)

        y = 20
        for row in self.rows:
            display.text(row.formatted_text(), 0, y, 1)
            y += self.row_height


class Display:
    def __init__(self, i2c):
        self.device = SH1106_I2C(128, 64, I2C(i2c), rotate=180)

        self.selected_view_index = None
        self.views = []

    def add_view(self, view: DisplayView):
        self.views.append(view)

        if self.selected_view_index is None:
            self.selected_view_index = 0

    def get_current_view(self) -> DisplayView:
        return self.views[self.selected_view_index] if self.selected_view_index is not None else None

    def update(self):
        current_view = self.get_current_view()

        if not current_view:
            return

        current_view.apply(self.device)

        self.device.show()
        sleep(0.1)
        self.device.fill(0)

    def next_view(self):
        self.selected_view_index = (self.selected_view_index + 1) % len(self.views)

    def prev_view(self):
        index = self.selected_view_index - 1
        if index == -1:
            self.selected_view_index = len(self.views) - 1
            return
        self.selected_view_index = index

    def set_next_button(self, button):
        button.on_press(self.next_view)

    def set_prev_button(self, button):
        button.on_press(self.prev_view)

    def clear(self):
        self.views = []
