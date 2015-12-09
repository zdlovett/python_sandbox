import threading
import time
import random
from collections import deque

class worker:
    def __init__(self, killEvent, queue, *args):
        self.args = args
        self.killEvent = killEvent
        self.queue = queue
        self.set = False

    def __call__(self):
        done = False
        while not done and not self.killEvent.isSet():
            try:
                done = self.work()
            except KeyboardInterrupt:
                self.killEvent.set()

    #for this example the args are [name, timeout]
    def work(self):
        done = False
        if self.set == False:
            self.set = True
            self.name = self.args[1]
            self.timeout = self.args[0]
            self.startTime = time.time()
        time.sleep(0.1)
        if time.time() - self.startTime > self.timeout:
            self.queue.append("hello from " + self.name)
            done = True
        return done

class manager:
    def __init__(self):
        self.threads = []
        self.queue = deque()
        self.kill = False
        self.killEvent = threading.Event()
        self.done = False

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

    def add_thread(self, *args):
        t = threading.Thread(target=worker(self.killEvent, self.queue, *args), args=())
        self.threads.append(t)

    def do_stuff(self):
        if len(self.queue) > 0:
            print self.queue.pop()

        if len(self.queue) == 0 and not threading.active_count() > 1:
            self.done = True

if __name__ == "__main__":
    prog = manager()
    prog.add_thread(1, "t1")
    prog.add_thread(3, "t2")
    prog.add_thread(6, "t3")

    prog.start_threads()
    try:
        while not prog.done and not prog.killEvent.isSet():
            prog.do_stuff()
    except KeyboardInterrupt:
        prog.killEvent.set()
