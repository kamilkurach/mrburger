import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(2, GPIO.IN)

while True:
  left_encoder = GPIO.input(3)
  right_encoder = GPIO.input(2)
  sleep(0.001)
  print("L: ", left_encoder, "R: ", right_encoder)

