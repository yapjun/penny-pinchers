import sqlite3

connection = sqlite3.connect('database.db')
with open('db_fiddle.sql' ) as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

