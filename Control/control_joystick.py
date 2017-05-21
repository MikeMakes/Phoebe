import RPi.GPIO as GPIO
import gamepad
GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

motor1 = GPIO.PWM(12, 480)
motor2 = GPIO.PWM(13, 480)


motor1.start(0)
motor2.start(0)

try:

	while True:
		gamepad = search_devices('Sony PLAYSTATION(R)3 Controller')
		for event in gamepad.read_loop():
			direccion = axe_move(ljX_axe)
			p_in = axe_move(r2_axe)+128
			print ("Valor de R2:{}".format(direccion))
			print ("Valor de joystick izquierdo:{}".format(p_in))
			if direccion = 0:
				motor1.start(p_in)
				motor2.start(p_in)
			if direccion < 0:
				p_der = p_in
				p_izq = p_der + 2*direccion
				if p_izq < 0:
					p_izq = 0
			if direccion > 0:
				p_izq = p_in
				p_der = p_izq - 2*direccion
				if p_der < 0:
					p_der = 0
			motor1.start(p_der)
			motor2.start(p_izq)
except KeyboardInterrupt:
	motor1.stop()
	motor2.stop()
	GPIO.cleanup()
