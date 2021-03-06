from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

try:
	i2c_bus = busio.I2C(SCL, SDA)	# Create the I2C bus interface.

	pca = PCA9685(i2c_bus)	# Create a simple PCA9685 class instance.

	pca.frequency = 50	# Set the PWM frequency to 50hz.

	leftm = pca.channels[0]
	dc=format(0,'#04x')

	while True:
		print ("Valor de duty cycle:{}".format(dc))
		print ("min: 0x0000 || MAX: 0xffff (65535)")
		print ("Esperando nueva duty cycle: ")
		dc=input()
		if dc=='on':
			dc=int('1999',16)	#6553
		elif dc=='off':
			dc=int('ccd',16)	#3277
		elif dc=='half':
			dc=int('1332',16)	#4914
		else:
			dc=int(dc,16)

		leftm.duty_cycle = dc
finally:
	pca.deinit()
