import sqlite3
from pathlib import Path

def create_database(*args):
    if args: 
        path = args[0]
    else:
        path = Path(__file__).parent

    path = path.joinpath('manager.db').resolve().as_posix()

    print(f'Creating database on path: {path}')
    con = sqlite3.connect(path) #connection
    cur = con.cursor()                  #cursor
    cur.execute('CREATE TABLE spending(date_time, name TEXT, value REAL)')
    cur.execute('CREATE TABLE incoming(date_time, name TEXT, value REAL)')

if __name__ == '__main__':
    pass