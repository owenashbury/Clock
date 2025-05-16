import math
import board
import busio
import adafruit_ad569x
import time

# NOT CURRENTLY IN USE
class Speaker:
    def __init__(self, i2c):
        # SPDX-FileCopyrightText: 2023 Liz Clark for Adafruit Industries
        # SPDX-License-Identifier: MIT
        self.i2c = i2c
        """Simple demo of writing a sine wave to the AD569x DAC."""

        # Initialize AD569x
        dac = adafruit_ad569x.Adafruit_AD569x(i2c)

        # Initialize I2C
        self.DAC_ADDRESS = 0x4C  # Verify this address matches your hardware setup

    def play_wav(self, filename):
        with open(filename, "rb") as wav_file:
            # Read WAV header
            header = wav_file.read(44)

            # Extract sample rate from header (bytes 24-27, little-endian)
            sample_rate = int.from_bytes(header[24:28], byteorder='little')
            sample_delay = 1 / sample_rate

            # Timing control
            next_time = time.monotonic()

            while True:
                # Read two bytes for 16-bit sample
                sample_bytes = wav_file.read(2)
                if not sample_bytes:
                    break  # End of file

                # Convert to signed integer (little-endian)
                sample = int.from_bytes(sample_bytes, byteorder='little')

                # Convert to DAC range (0-4095)
                # 1. Shift from signed 16-bit (-32768 to 32767) to unsigned (0-65535)
                # 2. Scale to 12-bit range (0-4095)
                unsigned_sample = sample + 32768
                dac_value = (unsigned_sample * 4095) // 65535  # Integer division

                # Create I2C message (command 0x30 + 16-bit data)
                data = (dac_value << 4).to_bytes(2, 'big')
                self.i2c.writeto(self.DAC_ADDRESS, bytes([0x30]) + data)

                # Maintain timing
                current_time = time.monotonic()
                sleep_time = next_time - current_time
                if sleep_time > 0:
                    time.sleep(sleep_time)
                next_time += sample_delay
