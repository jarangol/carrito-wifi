"""
Avanza, los dos motores marchan en el mismo sentido 
Gp 11: 1 |  Gp 16: 1   
Gp 13: 0 |  Gp 18: 0
"""
#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

adelante = 11
atras = 13
pwm = 12

GPIO.setup(adelante,GPIO.OUT)#Motor1
GPIO.setup(atras,GPIO.OUT)
GPIO.setup(pwm,GPIO.OUT)

GPIO.output(adelante,GPIO.HIGH)
GPIO.output(atras,GPIO.LOW)
GPIO.output(pwm,GPIO.HIGH)
  
  

