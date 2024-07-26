import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

while True:
  left_encoder = GPIO.input(23)
  right_encoder = GPIO.input(24)
  sleep(0.01)
  print("L: ", left_encoder, "R: ", right_encoder)

