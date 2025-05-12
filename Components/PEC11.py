from adafruit_seesaw import seesaw, rotaryio, digitalio

class Encoder:
    def __init__(self, i2c):
        self.i2c = i2c
        encoder = seesaw.Seesaw(i2c, 0x36)
