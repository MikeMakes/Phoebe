from tcp import mysocket

try:
	client=mysocket()			#New socket instance
	client.connect()	#Conect to IP:PORT (locahost for testing)
	while True:	
		client.send(raw_input())		#Send a string to the server (IT MUST BE A STRING)

finally:
	client.closesocket()			#Close connection
