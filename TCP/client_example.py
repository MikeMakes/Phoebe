from tcp import mysocket

try:
	client=mysocket()			#New socket instance
	client.connect("192.168.1.192",4200)	#Conect to IP:PORT (locahost for testing)
	client.send("This is a test")		#Send a string to the server (IT MUST BE A STRING)

finally:
	client.closesocket()			#Close connection
