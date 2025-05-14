from adafruit_seesaw import seesaw, rotaryio, digitalio

class Encoder:
    def __init__(self, i2c):
        self.i2c = i2c
        seesaw_encoder = seesaw.Seesaw(i2c, addr=0x36)
        seesaw_encoder.pin_mode(24, seesaw_encoder.INPUT_PULLUP)
        self.encoder_button = digitalio.DigitalIO(seesaw_encoder, 24)

        self.encoder = rotaryio.IncrementalEncoder(seesaw_encoder)
        last_position = None

    def getPressed(self):
        return self.encoder_button.value

