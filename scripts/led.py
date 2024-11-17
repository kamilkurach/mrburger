from time import sleep
import board
import neopixel

'''
https://docs.circuitpython.org/projects/neopixel/en/latest/

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

sudo python3 -m pip install --force-reinstall adafruit-blinka
'''
# LED Type: RGB WS2811 5mm

# GPIO10 SPI
pixel_pin = board.D10
num_pixels = 2
order = neopixel.RGB

led = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.95, auto_write=False, pixel_order=order)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

color_tab = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]

right_led = 0
left_led = 1

# right LED
for color in color_tab:
  for _ in range(3):
    led[right_led] = color
    led.show()
    sleep(0.1)
    led[right_led] = (0,0,0)
    led.show()
    sleep(0.1)

# left LED
for color in color_tab:
  for _ in range(3):
    led[left_led] = color
    led.show()
    sleep(0.1)
    led[left_led] = (0,0,0)
    led.show()
    sleep(0.1)

# both
for color in color_tab:
  for _ in range(3):
    led.fill((color))
    led.show()
    sleep(0.1)
    led.fill((0,0,0))
    led.show()
    sleep(0.1)
