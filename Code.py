import board
import time
import busio
from adafruit_ds3231 import DS3231
import displayio
import vectorio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_qualia.graphics import Graphics, Displays
from adafruit_qualia.peripherals import Peripherals


# from abc import ABC, abstractmethod
class RealTimeClock:
    def __init__(self, i2c):
        self.rtc = DS3231(i2c)

    def get(self):
        return self.rtc.datetime

    def setTime(self):
        pass

class App:
    def __init__(self):

        i2c = board.STEMMA_I2C()
        peripherals = Peripherals(i2c_bus=i2c)

        realTimeClock = RealTimeClock(i2c)
        current_time = realTimeClock.get()
        print(current_time)
        time.sleep(2)
        current_time = realTimeClock.get()
        print(current_time)

        # Initialize display (as above)

        screen = Graphics(Displays.ROUND21, default_bg=0x990099)
        display = screen.display

        # WebPage to show in the QR
        webpage = "http://www.adafruit.com"

        # QR size Information
        qr_size = 9  # Pixels
        scale = 10

        # Create a barcode
        screen.qrcode(
        webpage,
        qr_size=scale,
        x=(display.width // 2) - ((qr_size + 5) * scale),
        y=(display.height // 2) - ((qr_size + 4) * scale),
        )

        while True:
            if peripherals.button_up:
                peripherals.backlight = True
            if peripherals.button_down:
                peripherals.backlight = False
            time.sleep(0.1)
        #clockView = ClockView()
        #clockView.draw(screen)


'''
class View(ABC):
    @abstractmethod
    def draw(self):
        pass

class Input(ABC):
    @abstractmethod
    def get(self):
        pass

class Output(ABC):
    @abstractmethod
    def set(self):
        pass
'''

class ClockView():
    def draw(self, screen):
        clockView = displayio.Group()
        font = bitmap_font.load_font("/Roboto-Regular-47.pcf")
        text_label = label.Label(font, text="Hello Round Display!", color=0xFF00FF)

        clockView.append(text_label)
        screen.root_group = clockView

app = App()
