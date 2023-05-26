from LIB.SH1106 import SH1106_I2C
from machine import Pin, I2C
from time import sleep

class Display:
    def __init__(self, i2c):
        self.device = SH1106_I2C(128, 64, I2C(i2c), rotate=180)
        self.row_height = 20
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def update(self):
        y = 0
        for row in self.rows:
            self.device.text(row, 0, y, 1)
            y += self.row_height

        self.rows = []

        self.device.show()
        sleep(0.1)
        self.device.fill(0)