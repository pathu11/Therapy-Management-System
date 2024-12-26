# from flask import Flask
# from routes.auth import auth_blueprint
# from routes.cases import cases_blueprint
# from db import init_db

# def create_app():
#     app = Flask(__name__)
    
#     app.register_blueprint(auth_blueprint, url_prefix='/')
#     app.register_blueprint(cases_blueprint, url_prefix='/')
#     init_db()
    
#     return app


# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)

from flask import Flask
from routes.auth import auth_blueprint
from routes.cases import cases_blueprint
from db import init_db

# Initialize the Flask application
app = Flask(__name__)

# Register blueprints for authentication and cases
app.register_blueprint(auth_blueprint, url_prefix='/')
app.register_blueprint(cases_blueprint, url_prefix='/')

# Initialize the database
init_db()

