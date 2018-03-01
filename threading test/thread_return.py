from threading import Thread, Event
from queue import Queue
import time

def some_work(number, q, e):
    while not e.is_set():
        q.put(number * number)
        #time.sleep(0.5)

def kill_thread(e):
    time.sleep(10)
    e.set()

#results_q = Queue()
#kill_event = Event()
#num_threads = 1000
#threads = []
#for i in range(num_threads):
#    thread = Thread(target=some_work, args=(i, results_q, kill_event))
#    threads.append(thread)
#    thread.start()
#
#kt = Thread(target=kill_thread, args=(kill_event,))
#kt.start()
#
#threads.append(kt)
#
#for thread in threads:
#    result = thread.join()
#
#results = []
#while not results_q.empty():
#    results.append(results_q.get())
#
#print(len(results))


from multiprocessing.pool import Pool
def work(a):
    return a**2

with Pool() as pool:
    pool.map(work, range(50000000))
