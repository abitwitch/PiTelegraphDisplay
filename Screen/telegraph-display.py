import time
import sys
sys.path.append('./drive')
import SPI
import SSD1305

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

class Screen(object):
    def __init__(self):
        self.RST = None
        self.DC = 24
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0
        self.disp = SSD1305.SSD1305_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
        self.disp.begin()
        # Clear display.
        self.disp.clear()
        self.disp.display()
        # Create blank image for drawing.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('1', (self.width, self.height)) #'1' for 1-bit color
        self.draw = ImageDraw.Draw(self.image)
        self.padding = 0
        self.top = self.padding
        self.bottom = self.height-self.padding
        self.font = ImageFont.truetype('04B_08__.TTF',8)
    def writeLines(self,line1="",line2="",line3="",line4=""):
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
        x=0
        self.draw.text((x, self.top),    line1, font=font, fill=255)
        self.draw.text((x, self.top+8),  line2, font=font, fill=255)
        self.draw.text((x, self.top+16), line3, font=font, fill=255)
        self.draw.text((x, self.top+25), line4, font=font, fill=255)
        # Display
        self.disp.image(self.image)
        self.disp.display()



    