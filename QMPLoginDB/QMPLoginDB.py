import sqlite3

def create_QMP_database():
    print("CREATING TABLE QMP_Login_DB ....")
    conn = sqlite3.connect('QMP_Login_DB.db') #Opens Connection to SQLite database file.
    conn.execute('''CREATE TABLE QMP_Login_DB
                (FirstName       BLOB NOT NULL,
                 LastName        BLOB NOT NULL,
                 UserName        BLOB NOT NULL,
                 Password        BLOB NOT NULL
                );''')
    conn.commit()
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect('QMP_Login_DB.db')
    cursor = conn.cursor()
    params = (username,password)
    cursor.execute("INSERT INTO QMP_Login_DB VALUES (?,?,?,?)",params)
    conn.commit()
    print('User Creation Successful')
    conn.close()

def data_retrieval(username,password):
    conn = sqlite3.connect('QMP_Login_DB.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM QMP_Login_DB WHERE UserName =:NAME",{'NAME':username})
    if cur.fetchone()[1] == password:
        print('LogIn Successful')

def data_update(username):
    conn = sqlite3.connect('QMP_Login_DB.db')
    cur = conn.cursor()
    password = input("Enter the new password")
    cur.execute("""UPDATE QMP_Login_DB SET PASSWORD = :PASSWORD WHERE NAME =:NAME """,{'PASSWORD':password,'NAME':username})
    print("Update Successful")
    conn.commit()
    conn.close()

def data_delete(username):
    conn = sqlite3.connect('QMP_Login_DB.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM QMP_Login_DB WHERE NAME =:NAME """,{'NAME':username})
    print("User deletion Successful")
    conn.commit()
    conn.close()