# Luke Duran
# 04/06/25

import sqlite3

conn = sqlite3.connect('customers.db')  #Creates the file
cursor = conn.cursor()  # connects the file

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        contact_method TEXT
    )
''')

conn.commit() # Save changes
conn.close() # Close connection

