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
    print "Connection to port: ", port
except IndexError:
    port = 14570
    print "No port given, setting port: ", port

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))

while 1:
    data, address = s.recvfrom(1024)
    #print "got message of lenght: ", len(data), " from " ,address
    parse_sticks(data)
