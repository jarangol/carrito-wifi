import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

adelante = 11
atras = 13
pwm = 12

GPIO.setup(adelante,GPIO.OUT)#Motor1
GPIO.setup(atras,GPIO.OUT)
GPIO.setup(pwm,GPIO.OUT)

GPIO.output(adelante,GPIO.LOW)
GPIO.output(atras,GPIO.HIGH)
GPIO.output(pwm,GPIO.HIGH)
  
  

