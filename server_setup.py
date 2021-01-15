import socket
import threading

def connect_function(socket):
	finished = False
	while not finished:
		message = socket.recv(2049).decode()
		if message == "###":
			finished = true
			socket.close()
		else:
			user, text = message.split("_", 1)
			print(f"{user}: {text}")

	print("Connection ended")



class Server:
	def __init__(self, port):
		self.listener = socket.socket()
		self.listener.bind(('',port))
		self.current_connections = []
	
	def start(self):
		self.listener.listen(5)
		
		while True:
			server_socket, con_data = self.listener.accept()
			print(f"Connection from {con_data[0]}")
			new_thread = threading.Thread(target = connect_function, args = (server_socket,))
			new_thread.start()
			self.current_connections.append(new_thread)