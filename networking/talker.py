from socket import *
import sys
import time

try:
    port = int(sys.argv[2])
    print "Connected to port:", port
except IndexError:
    port = 12345
    print "No port given, setting port to:", port

try:
    host = sys.argv[1]
    print "setting host to:", host
except IndexError:
    host = 'localhost'
    print "No host given, setting host to:", host

try:
    action = sys.argv[3]
    print "setting action to", action
except IndexError:
    action = "A"
    print "no action given, setting action to A"

try:
    subport = sys.argv[4]
except IndexError:
    subport = '12345'
    print "No subport given, setting port to:", subport


s = socket(AF_INET, SOCK_DGRAM)
done = False
if s > 0:
    while not done:
        try:
            s.sendto(action + subport, (host, port) )
        except:
            pass
        else:
            done = True
            time.sleep(1)
