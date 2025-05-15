import displayio
import math
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

class AlarmSetView:
    def __init__(self):
        self.view_group = displayio.Group()
        font = bitmap_font.load_font("/Arial_16.bdf")

        self.minutes_past_midnight = 0

        self.text_label = label.Label(
            font,
            text="Set alarm time by rotating the button",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240)
        )

        self.time_label = label.Label(
            font,
            text="00:00",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240 + 50)
        )
        self.view_group.append(self.time_label)

    def draw(self, screen):
        screen.root_group = self.view_group
        screen.refresh()

    def stringFromMinutes(self):
        hours = math.floor(self.minutes_past_midnight / 60)
        minutes = self.minutes_past_midnight % 60
        updatedString = str(hours)+":"+str(minutes)
        print("updated string: "+updatedString)
        return updatedString

    def changeMinutes(self, minutes_delta):
        print("adding to minutes: "+str(minutes_delta))
        proposedNewMinutes = self.minutes_past_midnight + minutes_delta
        self.minutes_past_midnight = max(0, proposedNewMinutes) % (24 * 60)
        print("minutes past midnight is now "+str(self.minutes_past_midnight))
        self.time_label.text = self.stringFromMinutes()



