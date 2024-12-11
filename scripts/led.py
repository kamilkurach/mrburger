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

# init LEDs
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

# right & left turn signal (YELLOW)
def right_turn(pulses):
  for _ in range(pulses):
    led[0] = YELLOW
    led[1] = YELLOW
    led.show()
    slow_beep()
    sleep(0.3)
    led[0] = BLACK
    led[1] = BLACK
    led.show()
    sleep(0.3)

right_turn(3)

def left_turn(pulses):
  for _ in range(pulses):
    led[4] = YELLOW
    led[5] = YELLOW
    led.show()
    slow_beep()
    sleep(0.3)
    led[4] = BLACK
    led[5] = BLACK
    led.show()
    sleep(0.3)

left_turn(3)

# stop light (RED)
def stop_light(duration):
  led.fill(RED)
  led.show()
  long_beep()
  sleep(duration)
  led.fill(BLACK)
  led.show()
  sleep(duration)

stop_light(2)

# torch light (WHITE) for low light conditions
def low_light(duration):
  led[0] = WHITE
  led[1] = WHITE
  led[2] = RED
  led[3] = RED
  led[4] = WHITE
  led[5] = WHITE
  led[6] = WHITE
  led[7] = WHITE
  led.show()
  sleep(duration)
  led.fill(BLACK)
  led.show()

low_light(1)

# RED & GREEN
def port_starboard(duration):
  led[0] = GREEN
  led[1] = GREEN
  led[2] = WHITE
  led[3] = WHITE
  led[4] = RED
  led[5] = RED
  led.show()
  sleep(duration)
  led.fill(BLACK)
  led.show()

port_starboard(1)

def end():
  led.fill(GREEN)
  led.show()
  sleep(2)
  led.fill(BLACK)
  led.show()

end()
