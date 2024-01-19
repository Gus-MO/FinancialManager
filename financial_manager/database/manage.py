import sqlite3
from pathlib import Path


class DataBase():
    '''
    Base class to manage databases
    ---------------------------------

    args

        database: a sqlite connection
    '''

    def __init__(self, name):
        self.name = name + '.db'
        self.connection, self.cursor = self.connect_database(self.name)

    def connect_database(self, name, *args):
        '''
        Connects to the database and returns it cursor
        Creats if necessary
        '''
        if args: 
            path = args[0]
        else:
            path = Path(__file__).parent
        
        path = path.joinpath(name).resolve()
        path_str = path.as_posix()
    
        # creating database tables
        if not path.exists():
            print('Database Not Found.')
            print('Creating...')
            print(f'Creating database on path: {path}')
    
            con = sqlite3.connect(path_str) #connection
            cur = con.cursor()              #cursor
    
            cur.execute("CREATE TABLE spending(date_time, name TEXT, value REAL)")
            cur.execute("CREATE TABLE incoming(date_time, name TEXT, value REAL)")
    
            return con, cur
    
        con = sqlite3.connect(path_str) #connection
        cur = con.cursor()              #cursor
    
        return con, cur

    def show_entries(self, table, *args):
        '''
        Take some filters as input and return the stored data
        '''
        if not args:
            data = self.cursor.execute(f"SELECT * FROM {table}")

        pass

        return data

    def insert(self, name, value, table):
        # Inserts a new entry to the given database
        try:
            value = float(value)
        except TypeError('Value input not a number value'):
            pass
        if type(name) != str and type(value) != float:
            # Insert some error checks
            pass
        
        print(f'Inserting new entry into {table}: {name}\t{value}')
        self.cursor.execute(f"INSERT INTO {table} VALUES (0, '{name}', {value})")
        self.connection.commit()
        #try:
        #    self.cursor.execute(f"INSERT INTO spending VALUES ('{name}', {value})")
        #    self.cursor.commit()
        #    print(f'Entry inserted.')
        #except:
        #    print('Error')
        #    pass

        return None
    
    def delete(self):
        # Delets a entry from the given database
        return None

    def alter(self):
        # Alters a entry from the given database
        return None