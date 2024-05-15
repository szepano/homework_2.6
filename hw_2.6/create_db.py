import sqlite3

def create_db():
    with open('tables_raw.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == '__main__':
    create_db()