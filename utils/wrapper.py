
from functools import wraps
from flask import request, jsonify
from utils.jwt_util import decode_jwt 

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 403
        
        if token.startswith('Bearer '):
            token = token[7:]
            
        try:
            decoded = decode_jwt(token)
            request.user = decoded  
        except ValueError as e:
            return jsonify({'error': str(e)}), 403
        return f(*args, **kwargs)
    return wrapper
