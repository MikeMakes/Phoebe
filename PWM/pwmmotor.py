import pwm

motor = GPIO.PWM(24, 480)
i=5
iant= 0
start(motor, 5)
while True:
	print ("Valor de i:{}".format(i))
	print ("Esperando nueva i: ")
	i=input()
	changedc(motor, i)
finally:
	end(motor)
	clean()
