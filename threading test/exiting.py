from threading import Thread, Event
from queue import Queue

import time, random

def worker(name, msg_q, kill_e):
    while not kill_e.is_set():
        msg_q.put(f"Hello from {name} at time {time.monotonic()}")
        time.sleep( random.random() * 10 )
    msg_q.put(f"{name} has finished looping.")

def main():
    threads = []
    messages = Queue()
    kill_e = Event()
    for i in range(10):
        t = Thread(target=worker, args=(i, messages, kill_e))
        t.start()
        threads.append(t)
    
    while not kill_e.is_set():
        try:
            msg = messages.get()
            print(msg)
        except KeyboardInterrupt:
            kill_e.set()
    
    print("Done looping, waiting for threads to join.")
    for i, t in enumerate(threads):
        print(f"Waiting for thread {i} to join...")
        t.join()
        print(f"{i} joined.")

    print("All threads joined.")


if __name__ == "__main__":
    main()