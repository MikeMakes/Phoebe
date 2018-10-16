from board import SCL, SDA
import busio
 
# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

try:
	i2c_bus = busio.I2C(SCL, SDA)	# Create the I2C bus interface.
 
	pca = PCA9685(i2c_bus)	# Create a simple PCA9685 class instance.
 
	pca.frequency = 50	# Set the PWM frequency to 50hz.
 
	lmotor = pca.channels[0]
	lmotordc = lmotor.duty_cycle
	i=float(0)
	lmotordc = i

        while True:
                print ("Valor de duty cycle:{}".format(i))
                print ("Esperando nueva duty cycle: ")
                i=input()
                lmotordc = i

finally:
	pca.deinit()
	clean()
