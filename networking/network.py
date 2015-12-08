

import time
import threading
from socket import *


"""the networking class does the following:
1) creates a server that will handle incoming messages
2) broadcasts the connection information for that server
3) listens for broadcasts from other network modules
4) create a client for the other network

The class makes the following avaliable:
1) get connections : returns a list of all connected remotes
2) sent to connection : sents the given data to selected remotes

"""

class network(object):
    def __init__(self):
        print "started networking module"
