import sqlite3 as s

connection = s.connect ("QMP_DB.db")
cursor = connection.cursor ()


#cursor.execute ("DROP TABLE users")
command = """CREATE TABLE 
            IF NOT EXISTS users 
            (name TEXT, 
            password TEXT, 
            UNIQUE(name));"""

cursor.execute (command)

cursor.execute ("INSERT OR IGNORE INTO users VALUES ('admin', 'password')")
cursor.execute ("INSERT OR IGNORE INTO users VALUES ('username', '123456')")

connection.commit()