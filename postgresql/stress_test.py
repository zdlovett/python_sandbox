
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
    row['rmse'] = 1.0
    row['factor'] = 500
    row['wavelength'] = 1000.0
    return row

def generate_data( bundle ):
    name, con, cur = bundle
    num_rows = 1#random.randint(1, 10)
    ld = []
    for _ in range(num_rows):
        ld.append( random_row( name ) )
    insert_dicts(con, cur, 'best16', ld)

def worker(name):
    con = psycopg2.connect(host='zachbookpro.local', database='best16', user='python', password='python', connect_timeout=5)
    cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    bundle = (name, con, cur) 

    num_inserts = random.randint(10000, 100000)
    print(f"Running worker {name} inserting {num_inserts} lds")
    for i in range( num_inserts ):
        generate_data( bundle )
    
    con.close()

#pool based
num_pools = 50
print(f"Starting {num_pools} pools")
with mp.Pool(num_pools) as pool:
    pool.map( worker, range(num_pools * 10) )

print("All connections have closed")
    
    

