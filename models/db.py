import sqlite3

DATABASE = '/tmp/mental_health.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with open('database/setup_db.sql', 'r') as f:
        query = f.read()
    conn = get_db()
    conn.executescript(query)
    conn.close()
