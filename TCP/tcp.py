import socket

class mysocket:
	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self,IP=None,PORT=None):
		if IP is None:
			IP = "192.168.1.192"
		if PORT is None:
			PORT = 4200
		self.sock.connect((IP,PORT))
	
	def accept(self)
		acceptedsocket, addr = s.accept()
		print "Connection address:", addr
		return acceptedsocket

	def send(self,msg="Test"):
		msg = str(msg)
		self.sock.send(msg)

	def receive(self,BUFFER):
		if BUFFER is None:
			BUFFER = 1024
		data = self.sock.recv(BUFFER)
		print "Received data:", data
		return data

	def closesocket(self):
		print "Closing connection"
		self.sock.close()

