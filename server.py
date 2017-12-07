import socket
import time

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 65565

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while(1):

	conn, addr = s.accept()
	print("Connection address: ", addr)
	print("Connection info: ", conn)
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print("Recieved data: ", data)
	conn.send(data) #echo
	time.sleep(5)
conn.close()

