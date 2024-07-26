import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#GPIO25 PWMA
GPIO.setup(25, GPIO.OUT)
#GPIO12 AIN2
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
#GPIO16 AIN1
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)

#sensors
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

pwm = GPIO.PWM(25, 50)
pwm.start(0)

def print_sensor_data():
  left_encoder = GPIO.input(23)
  right_encoder = GPIO.input(24)
  print("L: ", left_encoder, "R: ", right_encoder)

#pwm.ChangeDutyCycle(35)
#sleep(5)

while True:
  for dc in range(0, 101, 3):
    print_sensor_data()
    pwm.ChangeDutyCycle(dc)
    sleep(0.1)
  for dc in range(100, -1, -3):
    print_sensor_data()
    pwm.ChangeDutyCycle(dc)
    sleep(0.1)

pwm.stop()
GPIO.cleanup()
