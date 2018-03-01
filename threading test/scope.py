import threading
import random

message = "boop"

def worker(func):
    def wrapper(*args, **kwargs):
        m = message

        returned_rows = []
        for db in config.db_list:
            active_db = db
            try:
                returned_rows.append(func(*args, **kwargs))
            except Exception as e:
                log.error(e)
                continue

        active_db = None
        return returned_rows
    return wrapper



def execute(statement):
    if random.random() > 0.5:
        statement = False
    else:
        statement = [statement]
    return statement

def do_task():
    global message

    ret = execute("hello")
    if ret is not None:
        r2 = execute("Nice to meet you")
    else:
        r2 = execute("I suppose nobody is there.")
    a = [ret, r2, message]
    b = [i for i in a if a != None]
    return b





if __name__ == "__main__":
    print("hello")
    for i in range(10):
        print(do_task())
