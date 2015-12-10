
from socket import *
import threading
import manager
import time

"""args for the remote worker are [(address, port)]"""
class remote(manager.worker):
    def setup(self):
        pass

    """this class does the work of handleing the remote connection"""
    def work(self):
        done = True
        return done

"""args for the server are []"""
class server(manager.worker):
    def setup(self):
        self.soc = socket()
        host = socket.gethostname()
        s.bind((host, ''))

    def work(self):
        pass

"""broadcaster args are [port, message, interval]"""
class broadcaster(manager.worker):
    def setup(self):
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.port = self.args[0]
        self.message = self.args[1]
        self.interval = self.args[2]
        self.last_time = 0

    def send(self, this_time):
        self.last_time = this_time
        self.soc.sendto(self.message, ('<broadcast>', self.port))

    def work(self):
        done = False
        this_time = time.time()
        if self.interval < 0:
            done = True
            self.send(this_time)
        elif this_time - self.last_time > self.interval:
            self.send(this_time)
        return done

"""listener args are [port]"""
class listener(manager.worker):
    def setup(self):
        self.port = self.args[0]
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.bind(('', self.port))
        self.soc.settimeout(0.1)
        self.soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def work(self):
        try:
            data, address = self.soc.recvfrom(1024)
        except timeout:
            return False
        else:
            self.queue.append(("listener", data, address))
        return False #this thread will never finish, it will only be killed by the others

if __name__ == "__main__":
    prog = manager.manager()
    prog.add_thread(listener, 12345)
    prog.add_thread(broadcaster, 12345, "This is all you get", -1)
    prog.add_thread(broadcaster, 12345, "hello", 1)

    prog.start_threads()
    prog.run()
