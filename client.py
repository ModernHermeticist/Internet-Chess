import socket
import time

tcp_IP = '127.0.0.1'
tcp_PORT = 5005
buffer_SIZE = 500
message = 'Hello World!'


while(1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((tcp_IP, tcp_PORT))
	s.send(bytes(message, 'UTF-8'))
	data = s.recv(buffer_SIZE)
	s.close()
	print("Received data: ", data)
	time.sleep(5)