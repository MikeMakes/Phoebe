from gamepad import * 
from tcp import *

try:
	client = tcp.mysocket()
	client.connect("192.168.1.192", 4200)

	gamepad = search_devices('Sony PLAYSTATION(R)3 Controller')
	for event in gamepad.read_loop():
		p_deri = axe_move(r2_axe)
		if p_deri is not None:
			client.send("RIGHT")
			client.send(str(p_deri))
			print ("Valor de R2:{}".format(p_deri))

		p_izqi = axe_move(l2_axe)
		if p_izqi is not None:
			client.send("LEFT")
			client.send(str(p_izqi))
			print ("Valor de L2:{}".format(p_izqi))

except KeyboardInterrupt:
	client.send("EXIT")
	client.closesocket()
	clean()