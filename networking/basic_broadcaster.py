#!/usr/bin/env python
from socket import *

class broadcaster(object):
    port = 12345

    def __init__(self, port=None):
        if port is not None:
            self.port = port
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    def send(self, word):
        self.soc.sendto(word, ('<broadcast>', self.port))

    def close(self):
        self.soc.close()

if __name__ == "__main__":
    import time
    b = broadcaster()
    done = False
    while not done:
        try:
            b.send("hello!")
            time.sleep(1)
        except KeyboardInterrupt:
            print "stopping broadcaster"
            b.close()
            done = True
