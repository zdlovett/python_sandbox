
import random
import psycopg2
import psycopg2.extras
from datetime import datetime as dt

from threading import Thread, Event
import multiprocessing as mp

def insert_dicts(con, cur, table, entries):
    """
    Given table<string> and entries<[dict]>
    Generate all of the entry command for the given table and list of entries,
    and then insert them in one transaction.
    """
    commands = ""
    values = []
    for entry in entries:
        _names  = ','.join(entry.keys())
        _values = [entry[k] for k in entry.keys()]
        _placeholders = ','.join(['%s']*len(_values))
        commands += f"INSERT INTO {table}({_names}) VALUES ({_placeholders}) ON CONFLICT DO NOTHING;"
        values += _values
    cur.execute(commands, values)
    con.commit()

def random_row(name):
    row = {}
    row['timestamp'] = dt.now()
    row['hostname'] = f'{name}'
    row['rmse'] = random.random() * 100
    row['factor'] = random.randint(0, 1024)
    row['wavelength'] = random.random() * 1000
    return row

def generate_data( bundle ):
    name, con, cur = bundle
    
    num_rows = random.randint( 1, 100 )
    
    ld = []
    for _ in range(num_rows):
        ld.append( random_row( name ) )
    insert_dicts(con, cur, 'best16', ld)

def worker(bundle):
    print(f"Worker has bundle: {bundle}")
    num_inserts = random.randint(100, 10000)
    for i in range( num_inserts ):
        generate_data( bundle )

bundles = [] #(number, con, cur)
for i in range(50):
    con = psycopg2.connect(host='localhost', database='best16', user='python', password='python', connect_timeout=5)
    cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    bundles.append( (i, con, cur) )

print(f"Active cons:{len(bundles)}")

#print('spawning worker threads')
#workers = []
#for b in bundles:
#    t = Thread(target=worker, args=(b, 1000) )
#    t.start()
#    workers.append(t)
#print("workers spawned, waiting for work to finish")
#
##close everything
#for w in workers:
#    w.join()

#pool based
print("Starting pools")
with mp.Pool(5) as pool:
    pool.map( worker, bundles )

print("All work finished")
for i, con, cur in bundles:
     con.close()

print("All connections have closed")
    
    

