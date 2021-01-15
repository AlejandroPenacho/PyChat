import socket

class ChatService():
	
	def __init__(self, user, ip, port):
		self.user = user
		self.client = socket.socket()
		self.client.connect((ip, port))
		
	def send(self, message):
		encoded_message = (self.user + "_" + message).encode()
		self.client.send(encoded_message)

	def close(self):
		self.client.send(b'###')
		self.client.close()