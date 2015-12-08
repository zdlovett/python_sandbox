from socket import *
import time

port = 12345
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))

while 1:
    data, address = s.recvfrom(1024)
    print data, address
