import displayio
import math
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

# AlarmSetView allows the user to set a new alarm time by turning the encoder rotary
class AlarmSetView:

    # set up the display
    def __init__(self):
        self.viewGroup = displayio.Group()
        font = bitmap_font.load_font("/Arial_16.bdf")

        self.minutesPastMidnight = 0

        self.textLabel = label.Label(
            font,
            text="Set alarm time by rotating the button",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240)
        )

        self.timeLabel = label.Label(
            font,
            text="00:00",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240 + 50)
        )
        self.viewGroup.append(self.timeLabel)

    # refresh the screen
    def draw(self, screen):
        screen.root_group = self.viewGroup
        screen.refresh()

    # converts the minutesPastMidnight to an HH:MM format for display
    def stringFromMinutes(self):
        hours = math.floor(self.minutesPastMidnight / 60)
        minutes = self.minutesPastMidnight % 60
        updatedString = str(hours)+":"+str(minutes)
        print("updated string: "+updatedString)
        return updatedString

    # let others read the current minutesPastMidnight setting
    def getMinutes(self):
        return self.minutesPastMidnight

    # change the current minutesPastMidnight setting
    def changeMinutes(self, minutesDelta):
        print("adding to minutes: "+str(minutesDelta))
        proposedNewMinutes = self.minutesPastMidnight + minutesDelta
        self.minutesPastMidnight = max(0, proposedNewMinutes) % (24 * 60)
        print("minutes past midnight is now "+str(self.minutesPastMidnight))
        self.timeLabel.text = self.stringFromMinutes()



