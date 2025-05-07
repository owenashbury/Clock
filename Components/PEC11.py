from adafruit_seesaw import seesaw, rotaryio, digitalio

class Encoder:
    def __init__(self, i2c):
        seesaw = seesaw.Seesaw(i2c, 0x36)
        seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
        print("Found product {}".format(seesaw_product))
