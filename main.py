import tcp
from ps3map import *
from evdev import InputDevice,list_devices, ecodes, KeyEvent, categorize

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
			return event.value


try:
	client = tcp.mysocket()
	client.connect("192.168.1.192",4200)

	gamepad1 = search_devices('Sony PLAYSTATION(R)3 Controller')
	for event in gamepad1.read_loop():
		axe = axe_move(r2_axe)
		if axe is not None:
			client.send("RIGHT")
			client.send(str(axe))
			print "RIGHT: " axe
		axe = axe_move(l2_axe)
		if axe is not None:
			client.send("LEFT")
			client.send(str(axe))
			print "RIGHT: " axe

finally:
	client.send("EXIT")
	client.closesocket()
