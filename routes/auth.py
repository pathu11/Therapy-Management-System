from flask import Blueprint, request, jsonify,session
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from jwt_util import generate_jwt
from wrapper import token_required

auth_blueprint = Blueprint('auth', __name__)
ab=auth_blueprint

@ab.route('/register', methods=['POST'])
def register():
    data = request.json
    fullname = data.get('fullname')
    username = data.get('username')
    password = data.get('password')

    if not fullname or not username or not password:
        return jsonify({'error': 'Fullname, username, and password are required!'}), 400

    if User.get_user(username): 
        return jsonify({'error': 'Username already exists!'}), 400

    hashed_password = generate_password_hash(password)

    User.create_user(fullname, username, hashed_password)
    return jsonify({'message': 'User registered successfully!'}), 201

@ab.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': ' user name, and password are required!'}), 400
    
    user = User.get_user(username)
    if not user:
        return jsonify({'error': 'Invalid credentials!'}), 401

    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials!'}), 401
    
    token = generate_jwt({'username': username, 'role': user['role']})

    return jsonify({'token': token})

@ab.route('/promote', methods=['POST'])
@token_required
def promote():
    data = request.json
    username = data.get('username')
    password=data.get('password')

    user = User.get_user(username)

    if not user:
        return jsonify({'error': 'Invalid credentials!'}), 401
    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials!'}), 401
    
    if user['role'] == 'Senior':
        return jsonify({'message': f'User {username} is already a Senior!'}),401
    User.update_role(username, 'Senior')
    return jsonify({'message': f'User {username} promoted to Senior!'}),200

@ab.route('/demote', methods=['POST'])
@token_required
def demote():
    data = request.json
    username = data.get('username')
    password=data.get('password')
    user = User.get_user(username)

    if not user:
        return jsonify({'error': 'Invalid credentials!'}), 401
    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials!'}), 401
    
    if user['role'] == 'Junior':
        return jsonify({'message': f'User {username} is already a Junior!'})
    User.update_role(username, 'Junior')
    return jsonify({'message': f'User {username} demoted to Junior!'}),200

