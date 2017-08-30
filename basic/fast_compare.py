import os, sys, time
from tqdm import tqdm

from threading import Thread
from queue import Queue
import pandas as pd

sys.path.append('/Users/zach/repo/codeVPCAMS/BEERCalStudyApps')
print(sys.path)

import config
from core import db, log_setup

config.db_name = 'beercal'

def quick_stat(raid, paths, q):
    results = []
    missing = 0
    for p in paths:
        s = time.monotonic()
        try:
            stats = [os.stat(f'/Users/zach/.storage_mounts/{raid}/{config.db_name}/{p}raw.raw')]
            stats.append(os.stat(f'/Users/zach/.storage_mounts/{raid}/{config.db_name}/{p}other.raw.gz'))
            stats.append(os.stat(f'/Users/zach/.storage_mounts/{raid}/{config.db_name}/{p}stats.json.gz'))
            result = {p : stats}
        except FileNotFoundError:
            result = {p:None}
            e = -1
        else:
            e = time.monotonic() - s

        q.put( (raid, result, e) )


if __name__ == "__main__":

    times = []

    print(f"DB Used:{config.db_name}")

    print("Getting dark samples from the database")
    darks = db.get_poc0_darks()
    print(len(darks))

    print("Pulling out the paths to the files...")
    paths = [d['filepath'] for d in tqdm(darks)]

    print("Starting to compare files.")
    results_q = Queue()
    r1_thread = Thread(target=quick_stat, args=('raid_1', paths, results_q))
    r2_thread = Thread(target=quick_stat, args=('raid_2', paths, results_q))

    r1_thread.start()
    r2_thread.start()

    for i in tqdm(range(len(paths)*2)):
        results = results_q.get()

    r1_thread.join()
    r2_thread.join()

    ld = [{'raid':r[0], 'result':r[1], 'time_taken':r[2] } for r in results]
    df = pd.DataFrame(ld)

    print(df)
