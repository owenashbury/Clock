import displayio
import math
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

class AlarmSetView:
    def __init__(self):
        self.hour = 0
        self.minutes = 0
        self.font = bitmap_font.load_font("/Arial_16.bdf")
        self.view_group = displayio.Group()
        font = bitmap_font.load_font("/Arial_16.bdf")

        self.minutes_past_midnight = 0

        self.text_label = label.Label(
            font = self.font,
            text = f"Set the Alarm: {self.hour:02d}:{self.minutes:02d}",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240)
        )

        self.view_group.append(self.text_label)

    def updateHour(self, hour):
        self.hour = hour % 24

    def updateMinutes(self, minutes):
        self.minutes = minutes % 60

    def getAlarm(self):
        hours = self.hour * 60
        minutes = self.minutes
        minutesPastMidnight = hours + minutes
        return minutesPastMidnight

    def overlapDetected(self):
        self.text_label.text = f"Overlap Detected."
        time.sleep(3)

    def draw(self, screen):
        screen.root_group = self.view_group
        self.text_label.text = f"Set the Alarm: {self.hour:02d}:{self.minutes:02d}"
        screen.refresh()


