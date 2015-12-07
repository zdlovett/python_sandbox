import threading
import time
import random
from collections import deque

class worker:
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

class main:
    def __init__(self):
        self.threads = []
        self.queue = deque()
        self.kill = False
        self.killEvent = threading.Event()

    def start_threads(self):
        for thread in self.threads:
            thread.start()

    def worker(self, timeout, name):
        startTime = time.time()
        while time.time() - startTime < timeout and not self.kill:
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                self.kill = True

        self.data.append("hello from " + name)

    def add_thread(self, timeout, name):
        t = threading.Thread(target=worker(name, timeout, self.killEvent, self.queue), args=())
        self.threads.append(t)

    def do_stuff(self):
        if len(self.queue) > 0:
            print self.queue.pop()

if __name__ == "__main__":
    prog = main()
    prog.add_thread(1, "t1")
    prog.add_thread(3, "t2")
    prog.add_thread(6, "t3")

    prog.start_threads()
    try:
        while threading.active_count() > 1 and not prog.killEvent.isSet():
            prog.do_stuff()
    except KeyboardInterrupt:
        prog.killEvent.set()
