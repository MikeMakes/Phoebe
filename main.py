import gamepad
import tcp

def map(bar, from_min, long from_max, long to_min, long to_max):
  return (bar - from_min) * (to_max - to_min) / (from_max - from_min) + to_min;

try:
	client = tcp.mysocket()
	client.connect("192.168.1.192",4200)

	gamepad = gamepad.search_devices('Sony PLAYSTATION(R)3 Controller')
	for event in gamepad.read_loop():
		axe = gamepad.axe_move(r2_axe)
		if axe is not None:
			client.send("RIGHT")
			axe = map(axe, 0, 255, 0, 100)
			client.send(str(axe))
		axe = gamepad.axe_move(l2_axe)
		if axe is not None:
			client.send("LEFT")
			axe = map(axe, 0, 255, 0, 100)
			client.send(str(axe))

finally:
	client.send("EXIT")
	client.closesocket()
