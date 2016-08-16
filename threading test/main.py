import threading
import time
import random
from collections import deque

class worker(object):
    def __init__(self, name, timeout, killEvent, queue):
        self.name = name
        self.timeout = timeout
        self.killEvent = killEvent
        self.queue = queue

    def __call__(self):
        startTime = time.time()
        while time.time() - startTime < self.timeout and not self.killEvent.isSet():
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                self.killEvent.set()
        self.queue.append("hello from " + self.name)

class manager(object):
    def __init__(self):
        self.threads = []
        self.queue = deque()
        self.killEvent = threading.Event()

    def add_thread(self, name, timeout):
        t = threading.Thread(target=worker(name, timeout, self.killEvent, self.queue), args=())
        self.threads.append(t)
        t.start()

    def do_stuff(self):
        if len(self.queue) > 0:
            print self.queue.pop()

if __name__ == "__main__":
    prog = manager()
    prog.add_thread(1, "t1")
    prog.add_thread(3, "t2")
    prog.add_thread(6, "t3")
    for i in range(1,100):
        prog.add_thread(1.0/i, str(i))

    try:
        while threading.active_count() > 1 and not prog.killEvent.isSet():
            prog.do_stuff()
    except KeyboardInterrupt:
        prog.killEvent.set()
