import RPi.GPIO as GPIO

def __init__(pin=24,freq=480):
	GPIO.setmode(GPIO.BCM)  
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
	
