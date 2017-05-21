from evdev import InputDevice,list_devices, ecodes, KeyEvent, categorize
from ps3map import *

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

def key_release(key):				#Return True when key is released
	if event.type == ecodes.EV_KEY:
		keyevent = categorize(event)
		if event.code == key and keyevent.keystate == KeyEvent.key_up:		#If 'key' released:
			return True
		else:
			return False

def axe_move(axe):				#Return axe's value when its move
	if event.type == ecodes.EV_ABS:		#Check if it is an absolute axis related event
		if event.code == axe:		#If 'axe' moved:
			return axevalue

if __name__=="__main__":
	gamepad = search_devices('Sony PLAYSTATION(R)3 Controller')
	for event in gamepad.read_loop():
		if key_press(square_key):
			print "Square pressed"
		axe = axe_move(ljX_axe)
		if axe is not None:
			print ("Left Joystick X move:{}".format(axe))
		axe = axe_move(ljY_axe)
		if axe is not None:
			print ("Left Joystick Y move:{}".format(axe))




