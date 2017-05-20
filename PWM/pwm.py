import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

def __init__(pin=24,freq=480):
	GPIO.setup(pin, GPIO.OUT)
	return GPIO.PWM(24, 480)

def start(pwm=None, dc=0):
	if pwm is None:
		break
	pwm.start(dc)

def end(pwm=None):
	if pwm is None:
		break
	pwm.stop()
	GPIO.cleanup()
	
if __name__ == "__main__" :
	pwm=__init__()
	for i in range(100):
		start(pwm,i)
		sleep(15)
	end(pwm)
	
