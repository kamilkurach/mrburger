import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
  state = GPIO.input(23)
  print(state)

