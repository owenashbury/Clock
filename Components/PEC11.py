from adafruit_seesaw import seesaw, rotaryio, digitalio

# The Encoder class sets up and communicates with the encoder, which has a button and a rotory input.
class Encoder:
    # encorder requires an i2c connection
    def __init__(self, i2c):
        self.i2c = i2c
        seesaw_encoder = seesaw.Seesaw(i2c, addr=0x36)
        seesaw_encoder.pin_mode(24, seesaw_encoder.INPUT_PULLUP)
        self.encoder_button = digitalio.DigitalIO(seesaw_encoder, 24)

        self.encoder = rotaryio.IncrementalEncoder(seesaw_encoder)
        last_position = None

    # read the current position of the encoder rotary
    def getPosition(self):
        return self.encoder.position

    # read the current pressed / not pressed state of the button
    def getPressed(self):
        return self.encoder_button.value
