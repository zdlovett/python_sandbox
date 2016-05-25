#!/usr/bin/python           # This is server.py file

#TODO: remove threads from list when thread finishes
#TODO: Add methods for sending data to drones.


import socket               # Import socket module
import threading
from collections import deque
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

def connection_worker(connection, done, queue):
    while not done:
        try:
            data = connection.recv(1024)
            if len(data)==0:
                done = True
            else:
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
start_time = time.time()
while not done:
    if time.time() - start_time > 1:
        print "number of threads", len(threads)
    try:
        connection, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        t = threading.Thread(target=connection_worker, args=(connection, done, incoming))
        t.start()
        threads.append(t)
    except KeyboardInterrupt:
        done = True
