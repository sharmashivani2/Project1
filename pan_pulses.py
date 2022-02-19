import RPi.GPIO as GPIO
from time import sleep
PUL = 23  # Stepper Drive Pulses
p_stop = 24


GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(p_stop, GPIO.OUT)
delay = 0.0005
GPIO.output(p_stop, GPIO.LOW)
while True:
    GPIO.output(PUL, GPIO.HIGH)
    sleep(delay)
    GPIO.output(PUL, GPIO.LOW)
    sleep(delay)
    
GPIO.cleanup()
