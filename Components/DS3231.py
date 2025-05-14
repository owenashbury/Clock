import time
from adafruit_ds3231 import DS3231

class RealTimeClock:
    def __init__(self, i2c):
        self.rtc = DS3231(i2c)

    def get(self):
        return self.rtc.datetime

    def setTime(self):
        pass

    def formatTime(self):
        time_struct = self.rtc.datetime
        hour = time_struct.tm_hour % 12
        hour = 12 if hour == 0 else hour
        am_pm = "AM" if time_struct.tm_hour < 12 else "PM"
        return f"{hour:02d}:{time_struct.tm_min:02d}:{time_struct.tm_sec:02d} {am_pm}\n"
