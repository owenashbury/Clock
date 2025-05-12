import board
import time
from adafruit_qualia.peripherals import Peripherals

# Import Component Classes
from Components.ST7701S import Screen
from Components.DS3231 import RealTimeClock
from Components.PEC11 import Encoder
from Components.AD5693R import Speaker

# Import View Classes
from Views.Time import TimeView

class App:
    def __init__(self):
        displayClass = Screen()
        display = displayClass.getScreen()
        clockView = TimeView()
        clockView.draw(display)

        i2c = board.STEMMA_I2C()
        peripherals = Peripherals(i2c_bus=i2c)
        rtc = RealTimeClock(i2c)
        speaker = Speaker(i2c)
        encoder = Encoder(i2c)
        # Usage example:
        while True:
            current_time = rtc.formatTime()
            clockView.update_time(current_time)
            clockView.draw(display)
            time.sleep(1)

app = App()
