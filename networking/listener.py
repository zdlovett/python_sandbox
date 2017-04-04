from socket import *
import time
import sys
import struct

def parse_sticks(data):
    sticks = struct.unpack("<Q9H", data)
    print "########################"
    for stick in sticks:
        print stick

try:
    port = int(sys.argv[1])
    print "Connected to port: ", port
except IndexError:
    port = 12345
    print "No port given, setting port: ", port

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('zachbookpro.local', port))

while 1:
    data, address = s.recvfrom(1024)
    print "got:", data, "from" ,address, "at time", time.time()
    data = data + ", " + str(time.time()) + ", " + address[0]
    with open("outfile.csv", 'a') as fd:
        fd.write(data + '\n')

#parse_sticks(data)
