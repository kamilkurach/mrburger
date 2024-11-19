#buzzer test

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def long_beep():
  GPIO.output(21, GPIO.HIGH)
  sleep(0.25)
  GPIO.output(21, GPIO.LOW)
  sleep(0.25)


def fast_beep():
  GPIO.output(21, GPIO.HIGH)
  sleep(0.05)
  GPIO.output(21, GPIO.LOW)
  sleep(0.05)

def slow_beep():
  GPIO.output(21, GPIO.HIGH)
  sleep(0.1)
  GPIO.output(21, GPIO.LOW)
  sleep(0.1)

#count = 5

#while count > 0:
#  fast_beep()
#  count-=1

#count = 5

#while count > 0:
#  slow_beep()
#  count-=1

