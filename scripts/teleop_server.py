import RPi.GPIO as GPIO
import pigpio
from time import sleep
import threading
import sys
import socket
from led import right_turn, left_turn, stop_light, forward_light_on, forward_light_off

GPIO.setmode(GPIO.BCM)

#GPIO12 PWMA
#GPIO.setup(12, GPIO.OUT)
#GPIO13 PWMB
#GPIO.setup(13, GPIO.OUT)

#GPIO4 STBY
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)

def backwards():
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

def forward():
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

def soft_stop():
  #GPIO6 AIN2
  GPIO.setup(6, GPIO.OUT)
  GPIO.output(6, GPIO.LOW)

  #GPIO5 AIN1
  GPIO.setup(5, GPIO.OUT)
  GPIO.output(5, GPIO.LOW)

  #GPIO26 BIN1
  GPIO.setup(26, GPIO.OUT)
  GPIO.output(26, GPIO.LOW)

  #GPIO19 BIN2
  GPIO.setup(19, GPIO.OUT)
  GPIO.output(19, GPIO.LOW)


#left sensor
GPIO.setup(22, GPIO.IN)
#right sensor
GPIO.setup(27, GPIO.IN)

#set gpio25 to 50Hz
#pwm_a = GPIO.PWM(12, 50)
#pwm_b = GPIO.PWM(13, 50)

PI = pigpio.pi()
#PI.hardware_PWM(12, 50000, 400000)
#PI.hardware_PWM(13, 50000, 400000)

#pwm_a.start(0)
#pwm_b.start(0)

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

'''
#t_r = threading.Thread(target=right_turn, args=(3,))
#t.start()
#t_l = threading.Thread(target=left_turn, args=(3,))

host = '192.168.5.111'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, 8080))
socket.listen(1)
connection, address = socket.accept()

current_state = None

forward_light_on()

while True:
  buffer = connection.recv(1024)
  if len(buffer) > 0:
    if str(buffer.decode()) == 'w':
      print(buffer)
      #soft_stop()
      #pwm_a.ChangeDutyCycle(0)
      #pwm_b.ChangeDutyCycle(0)
      #sleep(0.1)
      forward()
      PI.hardware_PWM(12, 50000, 400000)
      PI.hardware_PWM(13, 50000, 400000)
      #pwm_a.ChangeDutyCycle(40)
      #pwm_b.ChangeDutyCycle(40)
    elif str(buffer.decode()) == 'x':
      forward()
      PI.hardware_PWM(12, 50000, 650000)
      PI.hardware_PWM(13, 50000, 650000)
    elif str(buffer.decode()) == 's':
      print(buffer)
      soft_stop()
      #pwm_a.ChangeDutyCycle(0)
      #pwm_b.ChangeDutyCycle(0)
      PI.hardware_PWM(12, 50000, 0)
      PI.hardware_PWM(13, 50000, 0)
      sleep(0.2)
      backwards()
      PI.hardware_PWM(12, 50000, 400000)
      PI.hardware_PWM(13, 50000, 400000)
    elif str(buffer.decode()) == 'a':
      print(buffer)
      forward()
      #right_turn(1)
      #if t_r.is_alive() == False:
      #  t_r.start()
      #  t_r.join()
      PI.hardware_PWM(12, 50000, 550000)
      PI.hardware_PWM(13, 50000, 350000)
    elif str(buffer.decode()) == 'd':
      print(buffer)
      forward()
      #left_turn(1)
      #if t_l.is_alive() == False:
      #  t_l.start()
      #  t_l.join()
      PI.hardware_PWM(12, 50000, 350000)
      PI.hardware_PWM(13, 50000, 550000)
    elif str(buffer.decode()) == 'b':
      print(buffer)
      soft_stop()
      PI.hardware_PWM(12, 50000, 0)
      PI.hardware_PWM(13, 50000, 0)
      stop_light(1)
      forward_light_on()
    elif str(buffer.decode()) == 'q':
      print(buffer)
      soft_stop()
      #pwm_a.stop()
      #pwm_b.stop()
      PI.hardware_PWM(12, 50000, 0)
      PI.hardware_PWM(13, 50000, 0)
      forward_light_off()
      connection.close()
      #init STBY
      GPIO.output(4, GPIO.LOW)
      break
