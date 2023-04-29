import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS data 
            (id INTEGER PRIMARY KEY, text TEXT, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()
conn.close()