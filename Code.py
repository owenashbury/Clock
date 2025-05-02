import board
import time
import busio
from adafruit_ds3231 import DS3231
import displayio
import vectorio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_qualia.graphics import Graphics, Displays
from adafruit_qualia.peripherals import Peripherals

# Screen Libs
import dotclockframebuffer
from framebufferio import FramebufferDisplay
from displayio import release_displays


# from abc import ABC, abstractmethod
class RealTimeClock:
    def __init__(self, i2c):
        self.rtc = DS3231(i2c)

    def get(self):
        return self.rtc.datetime

    def setTime(self):
        pass

    def formatTime(self):
        time_struct = self.rtc.datetime
        print(time_struct)  # Fixed parentheses spacing

        hour = time_struct.tm_hour % 12
        hour = 12 if hour == 0 else hour
        am_pm = "AM" if time_struct.tm_hour < 12 else "PM"
        return(f"{hour:02d}:{time_struct.tm_min:02d}:{time_struct.tm_sec:02d} {am_pm}\n")

class App:
    def __init__(self):

        round21 = Round21()
        screen = round21.getScreen()

        clockView = ClockView()
        clockView.draw(screen)

        i2c = board.STEMMA_I2C()
        peripherals = Peripherals(i2c_bus=i2c)
        realTimeClock = RealTimeClock(i2c)

        while True:
            #Get updated time from RTC
            current_time = realTimeClock.formatTime()

            # Update display
            clockView.update_time(current_time)
            clockView.draw(screen)

            # Refresh rate control
            time.sleep(1)


        #i2c = board.STEMMA_I2C()
        #peripherals = Peripherals(i2c_bus=i2c)
        #realTimeClock = RealTimeClock(i2c)
        #current_time = realTimeClock.get()
        #print(current_time)
        #time.sleep(2)
        #current_time = realTimeClock.get()
        #print(current_time)


        #while True:
        #    if peripherals.button_up:
        #         peripherals.backlight = True
        #    if peripherals.button_down:
        #        peripherals.backlight = False
        #    time.sleep(0.1)



'''
class View(ABC):
    @abstractmethod
    def draw(self):
        pass

class Input(ABC):
    @abstractmethod
    def get(self):
        pass

class Output(ABC):
    @abstractmethod
    def set(self):
        pass
'''

class Round21:
    def __init__(self):
        release_displays()
        init_sequence_tl021wvc02 = bytes((
            0xff, 0x05, 0x77, 0x01, 0x00, 0x00, 0x10,
            0xc0, 0x02, 0x3b, 0x00,
            0xc1, 0x02, 0x0b, 0x02,
            0xc2, 0x02, 0x00, 0x02,
            0xcc, 0x01, 0x10,
            0xcd, 0x01, 0x08,
            0xb0, 0x10, 0x02, 0x13, 0x1b, 0x0d, 0x10, 0x05, 0x08, 0x07, 0x07, 0x24, 0x04, 0x11, 0x0e, 0x2c, 0x33, 0x1d,
            0xb1, 0x10, 0x05, 0x13, 0x1b, 0x0d, 0x11, 0x05, 0x08, 0x07, 0x07, 0x24, 0x04, 0x11, 0x0e, 0x2c, 0x33, 0x1d,
            0xff, 0x05, 0x77, 0x01, 0x00, 0x00, 0x11,
            0xb0, 0x01, 0x5d,
            0xb1, 0x01, 0x43,
            0xb2, 0x01, 0x81,
            0xb3, 0x01, 0x80,
            0xb5, 0x01, 0x43,
            0xb7, 0x01, 0x85,
            0xb8, 0x01, 0x20,
            0xc1, 0x01, 0x78,
            0xc2, 0x01, 0x78,
            0xd0, 0x01, 0x88,
            0xe0, 0x03, 0x00, 0x00, 0x02,
            0xe1, 0x0b, 0x03, 0xa0, 0x00, 0x00, 0x04, 0xa0, 0x00, 0x00, 0x00, 0x20, 0x20,
            0xe2, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0xe3, 0x04, 0x00, 0x00, 0x11, 0x00,
            0xe4, 0x02, 0x22, 0x00,
            0xe5, 0x10, 0x05, 0xec, 0xa0, 0xa0, 0x07, 0xee, 0xa0, 0xa0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0xe6, 0x04, 0x00, 0x00, 0x11, 0x00,
            0xe7, 0x02, 0x22, 0x00,
            0xe8, 0x10, 0x06, 0xed, 0xa0, 0xa0, 0x08, 0xef, 0xa0, 0xa0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0xeb, 0x07, 0x00, 0x00, 0x40, 0x40, 0x00, 0x00, 0x00,
            0xed, 0x10, 0xff, 0xff, 0xff, 0xba, 0x0a, 0xbf, 0x45, 0xff, 0xff, 0x54, 0xfb, 0xa0, 0xab, 0xff, 0xff, 0xff,
            0xef, 0x06, 0x10, 0x0d, 0x04, 0x08, 0x3f, 0x1f,
            0xff, 0x05, 0x77, 0x01, 0x00, 0x00, 0x13,
            0xef, 0x01, 0x08,
            0xff, 0x05, 0x77, 0x01, 0x00, 0x00, 0x00,
            0x36, 0x01, 0x00,
            0x3a, 0x01, 0x60,
            0x11, 0x80, 0x64,
            0x29, 0x80, 0x32,
        ))

        board.I2C().deinit()
        i2c = busio.I2C(board.SCL, board.SDA) #, frequency=400_000)
        tft_io_expander = dict(board.TFT_IO_EXPANDER)
        #tft_io_expander['i2c_address'] = 0x38 # uncomment for rev B
        dotclockframebuffer.ioexpander_send_init_sequence(i2c, init_sequence_tl021wvc02, **tft_io_expander)
        i2c.deinit()

        tft_pins = dict(board.TFT_PINS)

        tft_timings = {
            "frequency": 16_000_000,
            "width": 480,
            "height": 480,
            "hsync_pulse_width": 20,
            "hsync_front_porch": 40,
            "hsync_back_porch": 40,
            "vsync_pulse_width": 10,
             "vsync_front_porch": 40,
            "vsync_back_porch": 40,
            "hsync_idle_low": False,
            "vsync_idle_low": False,
            "de_idle_high": False,
            "pclk_active_high": True,
            "pclk_idle_high": False,
        }

        fb = dotclockframebuffer.DotClockFramebuffer(**tft_pins, **tft_timings)
        self.screen = FramebufferDisplay(fb, auto_refresh=False)

    def getScreen(self):
        return self.screen

class ClockView():
    def __init__(self):
        self.view_group = displayio.Group()

        # Load font (make sure the font file path is correct)
        font = bitmap_font.load_font("/Arial_16.bdf")

        # Create text label
        self.text_label = label.Label(
            font,
            text="Hello World!",
            color=0xFFFFFF,  # White text
            anchor_point=(0.5, 0.5),  # Center anchor
            anchored_position=(240, 240)  # Center of 480x480 display
        )

        self.view_group.append(self.text_label)

    def update_time(self, current_time):
        """Update the displayed text with a variable"""
        self.text_label.text = current_time

    def draw(self, screen):
        """Update the display with the current view"""
        screen.root_group = self.view_group
        screen.auto_refresh = False
        screen.refresh()  # Manual refresh since auto_refresh is False

app = App()
