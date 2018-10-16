#This script has to be executed in the laptop
import tcp
from ps3map import *
from evdev import InputDevice,list_devices, ecodes, KeyEvent, categorize
#Next, we define some functions to be able to use the PS3 controller

def search_devices(name='Sony PLAYSTATION(R)3 Controller'):	#This will search 'name' through all the devices
	print("Searching:")
	print(repr(name))
	devices = [InputDevice(fn) for fn in list_devices()]
	for device in devices:
		print(device.fn, device.name, device.phys)
		if device.name == name:
			return device		#Return the device with name 'name'

def key_press(key):				#Return True when key is pressed
	if event.type == ecodes.EV_KEY:		#Check if it is a key related event
		keyevent = categorize(event)
		if event.code == key and keyevent.keystate == KeyEvent.key_down:	#If 'key' pressed:
			return True
		else:
			return False

def key_release(key):			#Return True when key is released
	if event.type == ecodes.EV_KEY:
		keyevent = categorize(event)
		if event.code == key and keyevent.keystate == KeyEvent.key_up:		#If 'key' released:
			return True
		else:
			return False

def axe_move(axe):				#Return axe's value when its move
	if event.type == ecodes.EV_ABS:		#Check if it is an absolute axis related event
		if event.code == axe:		#If 'axe' moved:
			return event.value

#This is the main part of the program. It connects to a TCP network created by Raspberry.
#From the PS3 controller, it detects the axes R2 and L2, then send the values to Raspberry and
#and finally it shows in screen which axe has been pressed and the value sent to Raspberry 
try:
	client = tcp.mysocket()
	client.connect("192.168.1.192",4200)

	gamepad1 = search_devices('Sony PLAYSTATION(R)3 Controller')
	for event in gamepad1.read_loop():
		axe = axe_move(r2_axe)
		if axe is not None:
			client.send("RIGHT")
			client.send(str(axe))
			print "RIGHT: ", axe
		axe = axe_move(l2_axe)
		if axe is not None:
			client.send("LEFT")
			client.send(str(axe))
			print "LEFT: ", axe

finally:
	client.send("EXIT")
	client.closesocket()
