import RPi.GPIO as GPIO
from time import sleep
PUL = 25  # Stepper Drive Pulses
t_stop=17


GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(t_stop, GPIO.OUT)
delay = 0.0005
GPIO.output(t_stop, GPIO.LOW)
while True:
    GPIO.output(PUL, GPIO.HIGH)
    sleep(delay)
    GPIO.output(PUL, GPIO.LOW)
    sleep(delay)
    
GPIO.cleanup()
