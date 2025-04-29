import board
import time
import busio
from adafruit_ds3231 import DS3231
import displayio
import vectorio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_qualia.graphics import Graphics, Displays


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
        #i2c = busio.I2C(board.SCL, board.SDA)
        #realTimeClock = RealTimeClock(i2c)
        #current_time = realTimeClock.get()
        #print(current_time)
        #time.sleep(2)
        #current_time = realTimeClock.get()
        #print(current_time)

        # Initialize display (as above)
        screen = Graphics(Displays.ROUND21, default_bg=None, auto_refresh=True)
        clockView = ClockView()
        clockView.draw(screen)

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
        while True:
            pass

app = App()
