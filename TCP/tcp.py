import socket

#Method for tcp connection, useful for client & server

class mysocket:
	def __init__(self, sock=None):			#This is invoked automatically
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock		

	def server(self,IP=None,PORT=None):		#Call this on the server side
		if IP is None:
			IP = "localhost"
		if PORT is None:
			PORT = 4200		
		self.sock.bind((IP, PORT))
		self.sock.listen(1)

	def accept(self):				#Accept the incoming connection to the server
		(connect, addr) = self.sock.accept()
		self.connection = connect		#New sockect connection
		self.addres = addr			#Client's address
		return connect				#Return the new socket connection object, just in case you need it

	def connect(self,IP=None,PORT=None):		#Connect the client to the server IP:PORT
		if IP is None:
			IP = "localhost"
		if PORT is None:
			PORT = 4200
		self.sock.connect((IP,PORT))
	
	def send(self,msg="Test"):			#Send a string to the server
		msg = str(msg)+"\n"
		self.sock.send(msg)

	def receive(self,BUFFER=None):			#Receive a string from the client
		if BUFFER is None:
			BUFFER = 1
		recv_buffer=""
		data=""
		while data != "\n":	
			data = self.connection.recv(BUFFER)
			recv_buffer = recv_buffer + data		
		return recv_buffer
		
	def closesocket(self):				#Close socket, must be called before exit the program
		print "Closing connection"
		self.sock.close()

