import sqlite3

class DataBase():
    '''
    Base class to manage databases
    ---------------------------------

    args

        database: a sqlite connection
    '''


    def __init__(self, database):
        self.database = database
        cursor = self.database.cursor()


    def insert(self):
        # Inserts a new entry to the given database
        return None
    
    def delete(self):
        # Delets a entry from the given database
        return None

    def alter(self):
        # Altesr a entry from the given database
        return None