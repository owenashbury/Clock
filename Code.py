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

# App creates and manages all of the views and components and runs the main loop to display and check inputs.
class App:
    def __init__(self):

        # create the screens
        displayClass = Screen()
        display = displayClass.getScreen()
        clockView = TimeView()
        clockView.draw(display)
        alarmView = AlarmSetView()
        alarmView.draw(display)

        # create the Alarmist, which manages the alarm setting
        alarmist = Alarmist()

        # start with the clock view active
        self.activeView = clockView

        # open i2c bus to be used to communicate with the components
        i2c = board.STEMMA_I2C()
        peripherals = Peripherals(i2c_bus=i2c)
        rtc = RealTimeClock(i2c)
        speaker = Speaker(i2c)

        encoder = Encoder(i2c)
        encoderButtonHeld = False

        # Add debounce to prevent issues with holding down the button
        lastButtonState = True
        debounceTime = 0.3
        lastCheck = time.monotonic()

        lastPosition = 0

        # Run Loop
        while True:
            time.sleep(1) # limit the polling rate

            # Update the clock
            currentTimeStruct = rtc.get()
            currentTime = rtc.formatTime(currentTimeStruct)
            clockView.updateTime(currentTime)
            self.activeView.draw(display)

            # check encoder position (rotation)
            position = -encoder.getPosition() # negate the position to make clockwise rotation positive

            if position != lastPosition:
                delta = position - lastPosition
                lastPosition = position
                print("Position: {}".format(position))
                if self.activeView == alarmView:
                    alarmView.changeMinutes(delta)
                    alarmView.draw(display)


            # Check button state with debouncing
            if time.monotonic() - lastCheck > debounceTime:
                currentState = encoder.getPressed()
                lastCheck = time.monotonic()


                # Only trigger on state change
                if currentState != lastButtonState:
                    if currentState:  # Button is pressed (pull-up logic)
                        print("button pressed")
                        if self.activeView == alarmView:
                            newAlarm = alarmView.getMinutes()
                            alarmist.addAlarm(newAlarm)
                            self.activeView = clockView
                        else:
                            self.activeView = alarmView
                    lastButtonState = currentState

app = App()
