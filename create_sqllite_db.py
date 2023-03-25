import sqlite3 as s

connection = s.connect ("QMP_DB.db")
cursor = connection.cursor ()


cursor.execute ("DROP TABLE dropdownlist")
command = """CREATE TABLE 
            IF NOT EXISTS users 
            (name TEXT, 
            password TEXT, 
            UNIQUE(name));"""

cursor.execute (command)

dropdownlist = """CREATE TABLE 
            IF NOT EXISTS dropdownlist 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            UNIQUE(name));"""

cursor.execute (dropdownlist)

cursor.execute ("INSERT OR IGNORE INTO users VALUES ('admin', 'password')")
cursor.execute ("INSERT OR IGNORE INTO users VALUES ('username', '123456')")

cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('QueryType')")
cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('Schemas')")
cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('Tables')")
cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('Columns')")
cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('FilterConditions')")
cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('JoinsUsed')")
cursor.execute ("INSERT OR IGNORE INTO dropdownlist (name) VALUES ('AllMetadata')")

connection.commit()