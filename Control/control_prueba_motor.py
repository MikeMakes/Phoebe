import RPi.GPIO as GPIO
import gamepad
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)

motor = GPIO.PWM(24, 480)

motor.start(0)
gamepad = search_devices('Sony PLAYSTATION(R)3 Controller')
for event in gamepad.read_loop():
	potencia = axe_move(r2_axe)+128
	motor.star(potencia)
	print ("Valor de R2:{}".format(potencia))
