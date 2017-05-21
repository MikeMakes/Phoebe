from tcp import mysocket

try:
	server = mysocket()			#New socket instance
	server.server("localhost",4200)		#Setup server in IP:PORT (localhost for testing)
	server.accept()				#Accept client connection
	data = server.receive()			#Receive data from client (ALWAYS A STRING)
	print "From client: ",data		#Print data (again because mysocket().receive() print it)

finally:
	server.closesocket()			#Close connection
