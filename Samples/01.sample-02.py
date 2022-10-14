import socket

in_addr=socket.gethostbyname(socket.gethostname())

print(in_addr)

#IP address 8bit.8bit.8bit.8bit, i.e. 32 bit 
#ex)10.104.192.40