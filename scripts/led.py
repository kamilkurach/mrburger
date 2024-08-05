from time import sleep
import board
import neopixel

'''
https://docs.circuitpython.org/projects/neopixel/en/latest/

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

sudo python3 -m pip install --force-reinstall adafruit-blinka
'''

# GPIO10 SPI
pixel_pin = board.D10 
num_pixels = 1
ORDER = neopixel.RGB

led = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.4, auto_write=False, pixel_order=ORDER
)

while True:
  led.fill((255, 0, 0))
  led.show()
  sleep(2)
  led.fill((0, 255, 0))
  led.show()
  sleep(2)
  led.fill((0, 0, 255))
  led.show()
  sleep(2)
