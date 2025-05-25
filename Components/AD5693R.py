import math
import board
import busio
import adafruit_ad569x
import time

class Speaker:
    def __init__(self, i2c):
        self.i2c = i2c
        # Initialize DAC properly as an instance variable
        self.dac = adafruit_ad569x.Adafruit_AD569x(i2c)
        self.DAC_ADDRESS = 0x4C

    def buzz(self):
        print('buzzing')
        # Zelda discovery jingle notes (frequency in Hz, duration in seconds)
        melody = [
            (784, 0.2),   # G5
            (1047, 0.2),  # C6
            (1319, 0.4),  # E6
        ]

        for freq, duration in melody:
            if freq == 0:  # Handle rests if needed
                time.sleep(duration)
                continue

            half_period = 1 / (2 * freq)
            start_time = time.monotonic()

            while (time.monotonic() - start_time) < duration:
                # Generate square wave using DAC
                self.dac.value = 65535  # High
                target = time.monotonic() + half_period
                while time.monotonic() < target:
                    pass  # Busy-wait for better timing accuracy

                self.dac.value = 0  # Low
                target = time.monotonic() + half_period
                while time.monotonic() < target:
                    pass

        self.dac.value = 0  # Ensure DAC is off after playing
        print('buzzed')
