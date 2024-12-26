from flask import Flask
from routes.auth import auth_blueprint
from routes.cases import cases_blueprint
from models.db import init_db

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(cases_blueprint, url_prefix='/cases')
    
    init_db()

    @app.route('/')
    def welcome():
        return "Welcome to the Mental Health Institute API!"

    return app

# app = create_app()
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)