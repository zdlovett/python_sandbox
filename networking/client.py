#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346

done = False
connected = False
while not done:
    try:
        if not connected:
            s.connect((host, port))
            connected = True
        else:
            s.send(str(time.time()))
            print s.recv(1024)
            time.sleep(1)
    except KeyboardInterrupt:
        done = True

s.close                     # Close the socket when done
