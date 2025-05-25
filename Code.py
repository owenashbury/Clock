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
from Views.Alarm import AlarmView
from Views.Set import SetView

# Import Alarmist
from Alarmist import Alarmist

class App:
    def __init__(self):
        displayClass = Screen()
        display = displayClass.getScreen()
        setView = SetView()
        clockView = TimeView()
        alarmSetView = AlarmSetView()
        alarmView = AlarmView()

        alarmist = Alarmist()

        activeView = clockView

        i2c = board.STEMMA_I2C()
        peripherals = Peripherals(i2c_bus=i2c)
        rtc = RealTimeClock(i2c)
        timeSet = False
        hoursSet = False

        speaker = Speaker(i2c)

        encoder = Encoder(i2c)
        lastPos = 0

        while timeSet == False:
            button_pressed = encoder.checkButton()

            if button_pressed and hoursSet == False:
                print('Hours Set')
                hoursSet = True
                encoder.resetPosition()

            elif button_pressed and hoursSet == True:
                rtc.setTime(setView.setTime())
                timeSet = True
                encoder.resetPosition()

                print('All Set')

            if not hoursSet and encoder.checkRotation() != lastPos:
                lastPos = encoder.checkRotation()
                setView.updateHour(lastPos)

            elif hoursSet and encoder.checkRotation() != lastPos:
                lastPos = encoder.checkRotation()
                setView.updateMinutes(lastPos)

            setView.draw(display)

        activeView = clockView

        # Run Loop
        while True:
            button_pressed = encoder.checkButton()

            if activeView == clockView:
                current_time_struct = rtc.get()
                current_time = rtc.formatTime(current_time_struct)
                clockView.update_time(current_time)

            if button_pressed:
                if activeView == alarmSetView:
                    # Use App
                    newAlarm = alarmView.getMinutes()
                    alarmist.addAlarm(newAlarm)
                    activeView = clockView
                    encoder.resetPosition()

                else:
                    activeView = alarmSetView

            if alarmist.checkAlarms(rtc.get()):
                    alarmView.draw(display)
                    speaker.buzz()
                    time.sleep(1)

            if activeView == alarmSetView:
                # Other initialization
                self.hoursSet = False
                self.alarmSet = False

                # Later in your view loop:
                lastPos = 0
                while self.alarmSet == False:
                    button_pressed = encoder.checkButton()

                    if button_pressed and self.hoursSet == False:
                        print('Hours Set')
                        self.hoursSet = True
                        encoder.resetPosition()

                    elif button_pressed and self.hoursSet == True:
                        if alarmist.addAlarm(alarmSetView.getAlarm()):
                            self.alarmSet = True
                            encoder.resetPosition()
                            print('All Set')
                            activeView = clockView
                        else:
                            alarmSetView.overlapDetected()

                    if not self.hoursSet and encoder.checkRotation() != lastPos:
                        lastPos = encoder.checkRotation()
                        alarmSetView.updateHour(lastPos)

                    elif self.hoursSet and encoder.checkRotation() != lastPos:
                        lastPos = encoder.checkRotation()
                        alarmSetView.updateMinutes(lastPos)

                    alarmSetView.draw(display)

            activeView.draw(display)

app = App()
