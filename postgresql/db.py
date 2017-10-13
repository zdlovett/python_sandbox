import psycopg2
import psycopg2.extras


def execute(statement, args=None, fetchall=False, cursor_factory=psycopg2.extras.RealDictCursor):

    for attempt in range(3):
        try:
            con = psycopg2.connect(host='localhost', database='best16', user='python', password='python', connect_timeout=5)
            break
        except Exception as e:
            print("failed to connect to db")
            if attempt == 2:
                raise e

    try:
        cur = con.cursor(cursor_factory=cursor_factory)
        cur.execute(statement, args)
        fetch = cur.fetchall if fetchall else cur.fetchone
        rows = fetch() if statement.lower().startswith('select') else None
    except Exception as e:
        con.close()
        print("failed to execute on db")
        raise e
    else:
        con.commit()
        con.close()

    return rows

def insert_dict(table, entry_dict):
    "Given a table name and a dict of values with the correct key:value names and types, commit it to the db."
    names  = ','.join(entry_dict.keys())
    values = [entry_dict[k] for k in entry_dict.keys()]
    placeholders = ','.join(['%s']*len(values))
    execute(f"INSERT INTO {table}({names}) VALUES ({placeholders}) ON CONFLICT DO NOTHING", values)

def insert_dicts(table, entries):
    """
    Given table<string> and entries<[dict]>
    Generate all of the entry command for the given table and list of entries,
    and then insert them in one transaction.
    """
    commands = ""
    values = []
    for entry in entries:#TODO:Nice to have, do a check on the incoming dictlen and break it up into smaller commands
        _names  = ','.join(entry.keys())
        _values = [entry[k] for k in entry.keys()]
        _placeholders = ','.join(['%s']*len(_values))
        commands += f"INSERT INTO {table}({_names}) VALUES ({_placeholders}) ON CONFLICT DO NOTHING;"
        values += _values
    execute(commands, values)


if __name__ == '__main__':
    import socket
    insert_dict('test', {'mycolumn': socket.gethostname()})
