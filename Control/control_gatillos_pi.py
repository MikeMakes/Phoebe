from pwm import *
from tcp import *
GPIO.setmode(GPIO.BCM)
def map(bar, from_min=0,  from_max=255,  to_min=5,  to_max=10):
  return (bar - from_min) * (to_max - to_min) / (from_max - from_min) + to_min;

GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

motor1 = GPIO.PWM(12, 50)
motor2 = GPIO.PWM(13, 50)

motor1.start(0)
motor2.start(0)

try:
	server = tcp.mysocket()
	server.server("192.168.1.192", 4200) #RPI IP
	server.accept

	exit = False

	while not exit:
		Input = server.recieve()
		if Input == "RIGHT":
			p_der = int(server.recieve())
			p_der = map(p_der)
			pwm.changedc(motor1, p_der)
		elif Input == "LEFT":
			p_izq = int(server.recieve())
			p_izq = map(p_izq)
			pwm.changedc(motor2, p_izq)
		elif Input == "EXIT":
			exit = True
finally:
	motor1.stop()
	motor2.stop()
	GPIO.cleanup()
	server.closesocket()
	clean()


