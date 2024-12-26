from db import get_db

class User:
    @staticmethod
    def create_user(fullname,username, password, role='Junior'):
        db = get_db()
        db.execute('INSERT INTO users (fullname,username, password, role) VALUES (?,?, ?, ?)', (fullname,username, password, role))
        db.commit()

    @staticmethod
    def get_user(username):
        db = get_db()
        return db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    @staticmethod
    def update_role(username, role):
        db = get_db()
        db.execute('UPDATE users SET role = ? WHERE username = ?', (role, username))
        db.commit()

class Case:
    @staticmethod
    def add_case(name, description):
        db = get_db()
        db.execute('INSERT INTO cases (name, description) VALUES (?, ?)', (name, description))
        db.commit()

    @staticmethod
    def get_all_cases():
        db = get_db()
        return db.execute('SELECT * FROM cases').fetchall()
