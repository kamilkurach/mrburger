import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.IN)

while True:
  left_encoder = GPIO.input(22)
  right_encoder = GPIO.input(27)
  sleep(0.001)
  print("L: ", left_encoder, "R: ", right_encoder)

