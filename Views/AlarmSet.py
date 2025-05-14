import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

class AlarmSetView:
    def __init__(self):
        self.view_group = displayio.Group()
        font = bitmap_font.load_font("/Arial_16.bdf")

        self.text_label = label.Label(
            font,
            text="Set alarm time by rotating the button",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240)
        )
        self.view_group.append(self.text_label)

    def draw(self, screen):
        screen.root_group = self.view_group
        screen.auto_refresh = False
        screen.refresh()

# minutes_past_midnight = time_struct.tm_hour * 60 + time_struct.tm_min
