#!/usr/bin/env python
from socket import *
from basic_broadcaster import broadcaster
from basic_listener import listener

class sender(object):
    def __init__(self, ip=None, port=None):
        if port == None or ip == None:
            self.address = self.setup()
        else:
            self.address = (ip, port)
        self.soc = socket(AF_INET, SOCK_DGRAM)

    def setup(self):
        #have a listner at the setup port
        l = listener(port=12345)
        port_msg, sender_address = l.listen()
        return ( sender_address[0] , int(port_msg) )

    def send(self, word, address=None):
        if address == None:
            address = self.address
        return self.soc.sendto(word, address)

    def close(self):
        self.soc.close()

if __name__ == "__main__":
    import time
    s = sender()
    done = False
    while not done:
        try:
            word = "hello from sender at time:"
            word += str(time.time())
            s.send(word)
            time.sleep(1)
        except KeyboardInterrupt:
            s.close()
            done = True
