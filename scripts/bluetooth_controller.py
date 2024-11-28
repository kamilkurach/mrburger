import RPi.GPIO as GPIO
from time import sleep

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

#set gpio25 to 50Hz
pwm_a = GPIO.PWM(12, 50)
pwm_b = GPIO.PWM(13, 50)

pwm_a.start(0)
pwm_b.start(0)

while True:
  key = input()
  if key == 'w':
    forward()
    pwm_a.ChangeDutyCycle(55)
    pwm_b.ChangeDutyCycle(55)
  elif key == 's':
    backwards()
    pwm_a.ChangeDutyCycle(55)
    pwm_b.ChangeDutyCycle(55)
  elif key == 'a':
    turn_left()
    pwm_a.ChangeDutyCycle(50)
    pwm_b.ChangeDutyCycle(50)
  elif key == 'd':
    turn_right()
    pwm_a.ChangeDutyCycle(50)
    pwm_b.ChangeDutyCycle(50)
  elif key == 's':
    pwm_a.stop()
    pwm_b.stop()
    sleep(1)
  elif key == 'q':
    pwm_a.stop()
    pwm_b.stop()
    break
