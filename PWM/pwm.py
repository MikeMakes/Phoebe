import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

def __init__(pin=24,freq=480):
	GPIO.setup(pin, GPIO.OUT)
	return GPIO.PWM(24, 480)

def start(pwm=None, dc=0):
	if pwm is None:
		return None     #Must be substituted for exception
	pwm.start(dc)

def changedc(pwm=None, dc=0):
	if pwm is None:
		return None     #Must be substituted for exception
	pwm.ChangeDutyCicle(dc)

def changefrew(pwm=None, freq=480):
	if pwm is None:
		return None     #Must be substituted for exception
	pwm.ChangeFrequency(freq)

def end(pwm=None):
	if pwm is None:
		return None     #Must be substituted for exception
	pwm.stop()

def clean():
	GPIO.cleanup()
	
if __name__ == "__main__" :
	pwm=__init__()
	start(pwm,0)
	for i in range(100):
		changedc(pwm,i)
		sleep(15)
	end(pwm)
	clean()
	
