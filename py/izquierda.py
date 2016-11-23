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
pwm1 = 12

derecha = 15
izquierda = 16
pwm2 = 18

GPIO.setup(derecha,GPIO.OUT)#Motor1
GPIO.setup(izquierda,GPIO.OUT)
GPIO.setup(pwm2,GPIO.OUT)

GPIO.setup(adelante,GPIO.OUT)#Motor1
GPIO.setup(atras,GPIO.OUT)
GPIO.setup(pwm1,GPIO.OUT)

GPIO.output(derecha,GPIO.LOW)
GPIO.output(izquierda,GPIO.HIGH)
GPIO.output(pwm2,GPIO.HIGH)

GPIO.output(adelante,GPIO.HIGH)
GPIO.output(atras,GPIO.LOW)
GPIO.output(pwm1,GPIO.HIGH)
 
  

