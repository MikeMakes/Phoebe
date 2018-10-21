from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

def mapp(bar, from_min,  from_max,  to_min,  to_max):
  return (bar - from_min) * (to_max - to_min) / (from_max - from_min) + to_min;


try:
	i2c_bus = busio.I2C(SCL, SDA)	# Create the I2C bus interface.

	pca = PCA9685(i2c_bus)	# Create a simple PCA9685 class instance.

	pca.frequency = 50	# Set the PWM frequency to 50hz.

	leftm = pca.channels[0]
	dc=format(0,'#04x')

	while True:
		print ("hex (3277-6553):{}".format(dc))
		print ("min: 0% || MAX: 100%")
		print ("Esperando nuevo %")
		dc=input()
		dc=mapp(int(dc),0,100,3277,6553)
		dc=hex(int(dc))
		leftm.duty_cycle = int(dc,16)
finally:
	pca.deinit()
