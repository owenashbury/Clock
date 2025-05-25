from adafruit_seesaw import seesaw, rotaryio, digitalio
import time

class Encoder:
    def __init__(self, i2c):
        self.i2c = i2c
        seesaw_encoder = seesaw.Seesaw(i2c, addr=0x36)
        seesaw_encoder.pin_mode(24, seesaw_encoder.INPUT_PULLUP)
        self.encoder_button = digitalio.DigitalIO(seesaw_encoder, 24)
        self.encoder = rotaryio.IncrementalEncoder(seesaw_encoder)

        # Encoder Vars
        self.last_position = 0

        # Button Vars
        self.encoder_button_held = False
        # Add simple debounce variables
        self.last_button_state = True
        self.debounce_time = 1
        self.last_check = time.monotonic()

    def resetPosition(self):
        self.encoder.position = 0

    def checkRotation(self):
        position = self.encoder.position

        if position < 0:
            self.encoder.position = 0

        return self.encoder.position

    def checkButton(self):
        current_time = time.monotonic()
        current_state = self.encoder_button.value  # Read current state once

        # Check if debounce time has passed since the last state change
        if current_time - self.last_check > self.debounce_time:
            # Detect falling edge (button pressed, assuming active-low)
            if current_state != self.last_button_state:
                self.last_check = current_time
                self.last_button_state = current_state
                # Return True only on press (not release)
                if current_state == False:  # Adjust based on your button's wiring
                    print("Button pressed")
                    return True
        return False


