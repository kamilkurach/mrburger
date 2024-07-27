import RPi.GPIO as GPIO
from time import sleep
import threading
import sys

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

#set gpio25 to 50Hz
pwm = GPIO.PWM(25, 50)
pwm.start(0)

#set global vars initial values
PREV_TICK = GPIO.input(23)
TOTAL_TICKS = 0

#target distance in mm
TARGET = int(sys.argv[1])
print("TARGET: ", TARGET)

def calc_distance(tick_count):
  #returned distance in mm
  #wheel circumference 67 mm
  tick_per_revolution = 40
  distance = 67 * tick_count/tick_per_revolution
  return distance

def count_ticks(gpio):
  global TOTAL_TICKS
  global PREV_TICK
  while True:
    left_encoder = GPIO.input(gpio)
    if left_encoder == 1 and PREV_TICK == 0:
      TOTAL_TICKS += 1
    elif left_encoder == 0 and PREV_TICK == 1:
      TOTAL_TICKS += 1
    PREV_TICK = left_encoder
  #print("TT: ",TOTAL_TICKS,"PT: ",PREV_TICK)

def print_sensor_data():
  left_encoder = GPIO.input(23)
  right_encoder = GPIO.input(24)
  print("L: ", left_encoder, "R: ", right_encoder)

#count ticks from sensor in separate thread
gpio = 23
t = threading.Thread(target=count_ticks, args=(gpio,))
t.start()

while True:
  for dc in range(0, 101, 3):
    #print_sensor_data()
    if calc_distance(TOTAL_TICKS) > TARGET:
      pwm.stop()
      break
    pwm.ChangeDutyCycle(dc)
    print(calc_distance(TOTAL_TICKS))
    sleep(0.1)
  for dc in range(100, -1, -3):
    #print_sensor_data()
    if calc_distance(TOTAL_TICKS) > TARGET:
      pwm.stop()
      break
    pwm.ChangeDutyCycle(dc)
    print(calc_distance(TOTAL_TICKS))
    sleep(0.1)

pwm.stop()
GPIO.cleanup()

