import socket
import time

tcp_IP = '0.0.0.0'
tcp_PORT = 5005
buffer_SIZE = 65565

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((tcp_IP, tcp_PORT))
s.listen(1)

while(1):
	conn, addr = s.accept()
	print("Connection address: ", addr)
	print("Connection info: ", conn)
	data = conn.recv(buffer_SIZE)
	if not data: break
	print("Recieved data: ", data)
	conn.send(data) #echo
	time.sleep(5)
conn.close()

