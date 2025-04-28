import board
import time
import busio
from adafruit_ds3231 import DS3231

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
        i2c = busio.I2C(board.SCL, board.SDA)
        realTimeClock = RealTimeClock(i2c)
        current_time = realTimeClock.get()
        print(current_time)
        time.sleep(2)
        current_time = realTimeClock.get()
        print(current_time)


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

class ClockView(View):
    def draw(self):
        pass
'''

app = App()
