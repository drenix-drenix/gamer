import sqlite3

con = sqlite3.connect('workers.db')
cursor = con.cursor()
def CreateDB():
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, id INT, work INT)")
    con.commit()
def UpdateValue(val_name, new_val, id):
    for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0]+new_val
        cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        con.commit()
def UpdateValueMinus(val_name, new_val, id):
    for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0]-new_val
        cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        con.commit()
def InsertValue(name, id):
    cursor.execute(f'INSERT INTO users VALUES ("{name}", {id}, 0)')
    con.commit()
