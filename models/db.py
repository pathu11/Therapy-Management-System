import sqlite3
import os
DATABASE = 'database/mental_health.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    
    if not os.path.exists(DATABASE):
        os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    os.chmod('database', 0o777)  
    if os.path.exists(DATABASE):
        os.chmod(DATABASE, 0o666) 
        
    with open('database/setup_db.sql', 'r') as f:
        query = f.read()
    conn = get_db()
    conn.executescript(query)
    conn.close()
