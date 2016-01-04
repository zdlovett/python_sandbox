#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import threading
from collections import deque

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

def connection_worker(connection, done, queue):
    while not done:
        try:
            data = connection.recv(1024)
            print data
            connection.send(data)
        except KeyboardInterrupt:
            done = True

def data_worker(done, queue):
    while not done:
        try:
            print queue.pop()
        except IndexError:
            pass
        except KeyboardInterrupt:
            done = True

done = False
incoming = deque()
threads = []

#t = threading.Thread(target=data_worker, args=(done, incoming))
#t.start()
while not done:
    try:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        t = threading.Thread(target=connection_worker, args=(c, done, incoming))
        t.start()
        threads.append(t)
    except KeyboardInterrupt:
        done = True
