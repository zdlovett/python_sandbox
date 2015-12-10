import threading
import time
import random
from collections import deque

class worker:
    def __init__(self, killEvent, queue, *args):
        self.args = args
        self.killEvent = killEvent
        self.queue = queue

    def __call__(self):
        self.setup()
        done = False
        while not done and not self.killEvent.isSet():
            try:
                done = self.work()
            except KeyboardInterrupt:
                self.killEvent.set()

    def setup(self):
        self.name = self.args[1]
        self.timeout = self.args[0]
        self.startTime = time.time()

    #for this example the args are [name, timeout]
    def work(self):
        done = False
        time.sleep(0.1)
        if time.time() - self.startTime > self.timeout:
            self.queue.append("hello from " + self.name)
            done = True
        return done

#this shows how to make a class that will be spawned in it's own thread based on the worker class
class fast_worker(worker):
    def setup(self):
        self.name = self.args[1]
        self.timeout = self.args[0] / 10.0
        self.startTime = time.time()

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

    def add_thread(self, target, *args):
        t = threading.Thread(target=target(self.killEvent, self.queue, *args), args=())
        self.threads.append(t)

    """override this function depending on the management logic for the program"""
    def work(self):
        if len(self.queue) > 0:
            print self.queue.pop()

        if len(self.queue) == 0 and not threading.active_count() > 1:
            self.done = True

    def run(self):
        while not self.done and not self.killEvent.isSet():
            try:
                self.work()
            except KeyboardInterrupt:
                self.killEvent.set()


if __name__ == "__main__":
    prog = manager()
    prog.add_thread(worker, 1, "t1")
    prog.add_thread(worker, 3, "t2")
    prog.add_thread(fast_worker, 6, "t3")

    prog.start_threads()
    prog.run()
