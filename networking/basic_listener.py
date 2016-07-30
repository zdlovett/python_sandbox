#!/usr/bin/env python
from socket import *
from basic_broadcaster import broadcaster
import sys

class listener(object):
    def __init__(self, ip='', port=0):
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.bind((ip, port))
        if port == 0:
            self.setup()

    def setup(self):
        port_msg = str(self.soc.getsockname()[1])
        b = broadcaster()
        self.soc.settimeout(2)
        connected = False
        while not connected:
            b.send(port_msg)
            try:
                self.listen()
            except timeout:
                print "socket timeout, trying again..."
            except KeyboardInterrupt:
                connected = True
                b.close()
                self.close()
                sys.exit()
            else:
                connected = True
                print "connected"


    def listen(self):
        data, address = self.soc.recvfrom(2048)
        return data, address

    def close(self):
        self.soc.close()

if __name__ == "__main__":
    l = listener()
    done = False
    while not done:
        try:
            data, address = l.listen()
            print "got ", data, "from" , address
        except KeyboardInterrupt:
            done = True
            l.close()
