import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

# TimeView displays the basic clock with current time
class TimeView:

    # set up the display
    def __init__(self):
        self.viewGroup = displayio.Group()
        font = bitmap_font.load_font("/Arial_16.bdf")

        self.textLabel = label.Label(
            font,
            text="Hello World!",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(240, 240)
        )
        self.viewGroup.append(self.text_label)

    # update display to current time
    def updateTime(self, currentTime):
        self.textLabel.text = currentTime

    # refresh the display
    def draw(self, screen):
        screen.root_group = self.viewGroup
        screen.auto_refresh = False
        screen.refresh()
