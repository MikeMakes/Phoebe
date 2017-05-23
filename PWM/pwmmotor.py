import pwm

motor = GPIO.PWM(24, 480)
i=5;
start(motor, 5)
print ("Valor de i:{}".format(i))
changedc(motor, i)
raw_input()
	end(motor)
	clean()
