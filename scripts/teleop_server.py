import RPi.GPIO as GPIO
from time import sleep
import threading
import sys
import socket

GPIO.setmode(GPIO.BCM)

#GPIO12 PWMA
GPIO.setup(12, GPIO.OUT)
#GPIO13 PWMB
GPIO.setup(13, GPIO.OUT)

#GPIO4 STBY
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)

def backwards():
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

def forward():
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

def turn_left():
  #GPIO6 AIN2
  GPIO.setup(6, GPIO.OUT)
  GPIO.output(6, GPIO.HIGH)

  #GPIO5 AIN1
  GPIO.setup(5, GPIO.OUT)
  GPIO.output(5, GPIO.LOW)

  #GPIO26 BIN1
  GPIO.setup(26, GPIO.OUT)
  GPIO.output(26, GPIO.HIGH)

  #GPIO19 BIN2
  GPIO.setup(19, GPIO.OUT)
  GPIO.output(19, GPIO.LOW)

def turn_right():
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


#left sensor
GPIO.setup(22, GPIO.IN)
#right sensor
GPIO.setup(27, GPIO.IN)

#set gpio25 to 50Hz
pwm_a = GPIO.PWM(12, 50)
pwm_b = GPIO.PWM(13, 50)

pwm_a.start(0)
pwm_b.start(0)

#set global vars initial values
PREV_TICK = GPIO.input(22)
TOTAL_TICKS = 0
TARGET_REACHED = False

'''
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
  left_encoder = GPIO.input(22)
  right_encoder = GPIO.input(27)
  print("L: ", left_encoder, "R: ", right_encoder)


#count ticks from sensor in separate thread
gpio = 22
t = threading.Thread(target=count_ticks, args=(gpio,))
t.start()
'''

host = '192.168.5.104'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, 8080))
socket.listen(1)
connection, address = socket.accept()

while True:
  buffer = connection.recv(1024)
  if len(buffer) > 0:
    if str(buffer.decode()) == 'w':
      print(buffer)
      forward()
      pwm_a.ChangeDutyCycle(55)
      pwm_b.ChangeDutyCycle(55)
    elif str(buffer.decode()) == 's':
      print(buffer)
      backwards()
      pwm_a.ChangeDutyCycle(55)
      pwm_b.ChangeDutyCycle(55)
    elif str(buffer.decode()) == 'a':
      print(buffer)
      turn_left()
      pwm_a.ChangeDutyCycle(50)
      pwm_b.ChangeDutyCycle(50)
    elif str(buffer.decode()) == 'd':
      print(buffer)
      turn_right()
      pwm_a.ChangeDutyCycle(50)
      pwm_b.ChangeDutyCycle(50)
    elif str(buffer.decode()) == 'q':
      print(buffer)
      pwm_a.stop()
      pwm_b.stop()
      connection.close()
      break
