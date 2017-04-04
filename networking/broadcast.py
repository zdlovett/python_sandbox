from socket import *
import time

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
port = 5000

while 1:
    data = "hello at time: " + str(time.time())
    s.sendto(data, ('<broadcast>', port))
    time.sleep(2)
