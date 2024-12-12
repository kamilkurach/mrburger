from time import sleep
import board
import neopixel
from buzzer import slow_beep, long_beep

'''
https://docs.circuitpython.org/projects/neopixel/en/latest/

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

sudo python3 -m pip install --force-reinstall adafruit-blinka
'''
# LED Type: RGB WS2812 SMD

# GPIO10 SPI
pixel_pin = board.D10
num_pixels = 8
order = neopixel.GRB

led = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.95, auto_write=True, pixel_order=order)

# STATUS LED
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

color_tab = [RED, GREEN, BLUE]

for color in color_tab:
  for i in range(num_pixels):
    led[i] = color
    led.show()
    sleep(0.02)
    led[i] = BLACK
    led.show()

led.fill(GREEN)
led.show()
slow_beep()
sleep(0.5)
led.fill(BLACK)
led.show()
