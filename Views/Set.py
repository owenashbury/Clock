import displayio
import time
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

class SetView:
    def __init__(self):
        self.view_group = displayio.Group()
        self.font = bitmap_font.load_font("/Arial_16.bdf")
        self.hour = 0
        self.minutes = 0

        self.text_label = label.Label(
            font = self.font,
            text = f"Set the Time: {self.hour:02d}:{self.minutes:02d}",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240)
        )
        self.view_group.append(self.text_label)



    def updateHour(self, hour):
        self.hour = hour % 24

    def updateMinutes(self, minutes):
        self.minutes = minutes % 60

    def setTime(self):
        # Set the time (example: 2023-10-15 14:30:00)
        newTime = time.struct_time(
            (2025, 5, 25,  # Year, Month, Day
            self.hour, self.minutes, 0,     # Hour, Minute, Second
            -1, -1, -1)    # Ignore weekday, yearday, and isdst
        )

        return newTime

    def draw(self, screen):
        screen.root_group = self.view_group
        self.text_label.text = f"Set the Time: {self.hour:02d}:{self.minutes:02d}"
        screen.refresh()
