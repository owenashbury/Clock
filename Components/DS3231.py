import time
from adafruit_ds3231 import DS3231

# RealTimeClock manages the intilization and communication with the RealTimeClock component, which keeps the time accurately.
class RealTimeClock:
    # the RTC requires and i2c connection to communicate with the program
    def __init__(self, i2c):
        self.rtc = DS3231(i2c)

    # returns the current time
    def get(self):
        return self.rtc.datetime

    # not yet implemented
    def setTime(self):
        pass

    # get a formatted string version from a time struct
    def formatTime(self, timeStruct):
        hour = timeStruct.tm_hour % 12
        hour = 12 if hour == 0 else hour
        amPm = "AM" if timeStruct.tm_hour < 12 else "PM"
        return f"{hour:02d}:{timeStruct.tm_min:02d}:{timeStruct.tm_sec:02d} {am_pm}\n"
