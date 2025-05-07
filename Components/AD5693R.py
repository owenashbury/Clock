import math
import board
import busio
import adafruit_ad569x

class Speaker:
    def __init__(self, i2c):
        # SPDX-FileCopyrightText: 2023 Liz Clark for Adafruit Industries
        # SPDX-License-Identifier: MIT

        # Initialize AD569x
        dac = adafruit_ad569x.Adafruit_AD569x(i2c)

        # length of the sine wave
        LENGTH = 100
        # sine wave values written to the DAC
        value = [
            int(math.sin(math.pi * 2 * i / LENGTH) * ((2**15) - 1) + 2**15)
            for i in range(LENGTH)
        ]

        while True:
            for v in value:
                dac.value = v


