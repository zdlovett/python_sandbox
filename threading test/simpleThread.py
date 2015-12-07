import threading
import time

class simpleThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(simpleThread,self).__init__(group=group, target=target, name=name, verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        time.sleep(self.args[1])
        print "hello from thread " + self.args[2]
