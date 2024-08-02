import RPi.GPIO as GPIO
from time import sleep
import threading
import sys

GPIO.setmode(GPIO.BCM)

#GPIO12 PWMA
GPIO.setup(12, GPIO.OUT)
#GPIO13 PWMB
GPIO.setup(13, GPIO.OUT)

#GPIO4 STBY
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)

try:
  if sys.argv[2] == "-forward":
    print("init forward")

    #GPIO6 AIN2
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)

    #GPIO5 AIN1
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)

    #GPIO26 BIN1
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH)

    #GPIO19 BIN2
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.LOW)

  elif sys.argv[2] == "-backwards":
    print("init backwords")

    #GPIO6 AIN2
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.HIGH)

    #GPIO5 AIN1
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.LOW)

    #GPIO26 BIN1
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.LOW)

    #GPIO19 BIN2
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)

  elif sys.argv[2] == "-turn":

    print("init turn")
    #GPIO6 AIN2
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)

    #GPIO5 AIN1
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)

    #GPIO26 BIN1
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.LOW)

    #GPIO19 BIN2
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)

except IndexError as e:
    print("Missing param: -forwad -backwards -turn")
    sys.exit(0)

#sensors
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

#set gpio25 to 50Hz
pwm_a = GPIO.PWM(12, 50)
pwm_b = GPIO.PWM(13, 50)

pwm_a.start(0)
pwm_b.start(0)

#set global vars initial values
PREV_TICK = GPIO.input(23)
TOTAL_TICKS = 0
TARGET_REACHED = False

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
  global TARGET_REACHED
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

while t.is_alive() and TARGET_REACHED is False:

  for dc in range(0, 101, 3):
    #print_sensor_data()
    if calc_distance(TOTAL_TICKS) > TARGET:
      pwm_a.stop()
      pwm_b.stop()
      TARGET_REACHED = True
      break
    pwm_a.ChangeDutyCycle(dc)
    pwm_b.ChangeDutyCycle(dc)
    print(calc_distance(TOTAL_TICKS))
    sleep(0.1)
  for dc in range(100, -1, -3):
    #print_sensor_data()
    if calc_distance(TOTAL_TICKS) > TARGET:
      pwm_a.stop()
      pwm_b.stop()
      TARGET_REACHED = True
      break
    pwm_a.ChangeDutyCycle(dc)
    pwm_b.ChangeDutyCycle(dc)
    print(calc_distance(TOTAL_TICKS))
    sleep(0.1)

print("exit")
t.join(timeout=2)
if t.is_alive():
  GPIO.cleanup()
  sys.exit()
