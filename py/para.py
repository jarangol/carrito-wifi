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

GPIO.setup(derecha,GPIO.OUT)#Motor direccion
GPIO.setup(izquierda,GPIO.OUT)
GPIO.setup(pwm2,GPIO.OUT)

GPIO.setup(adelante,GPIO.OUT)#Motor avance
GPIO.setup(atras,GPIO.OUT)
GPIO.setup(pwm1,GPIO.OUT)

GPIO.output(derecha,GPIO.LOW)
GPIO.output(izquierda,GPIO.LOW)
GPIO.output(pwm2,GPIO.LOW)

GPIO.output(adelante,GPIO.LOW)
GPIO.output(atras,GPIO.LOW)
GPIO.output(pwm1,GPIO.LOW)

GPIO.cleanup()  

