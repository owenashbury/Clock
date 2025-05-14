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
from Views.AlarmSet import AlarmSetView

# Import Alarmist
from Alarmist import Alarmist

class App:
    def __init__(self):
        displayClass = Screen()
        display = displayClass.getScreen()
        clockView = TimeView()
        clockView.draw(display)
        alarmView = AlarmSetView()
        alarmView.draw(display)

        alarmist = Alarmist()

        self.activeView = clockView

        i2c = board.STEMMA_I2C()
        peripherals = Peripherals(i2c_bus=i2c)
        rtc = RealTimeClock(i2c)
        speaker = Speaker(i2c)

        encoder = Encoder(i2c)
        encoder_button_held = False
        # Add simple debounce variables
        last_button_state = True
        debounce_time = 0.3
        last_check = time.monotonic()

        # Usage example:
        while True:
            time.sleep(1)
            current_time_struct = rtc.get()
            current_time = rtc.formatTime(current_time_struct)
            clockView.update_time(current_time)
            self.activeView.draw(display)
            # Check button state with debouncing
            if time.monotonic() - last_check > debounce_time:
                current_state = encoder.getPressed()
                last_check = time.monotonic()

                # Only trigger on state change
                if current_state != last_button_state:
                    if current_state:  # Button is pressed (pull-up logic)
                        #self.activeView = alarmView
                        print("button pressed")
                    last_button_state = current_state

app = App()
