import jwt
import datetime
import os
from dotenv import load_dotenv
from flask import request

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def generate_jwt(payload, expires_in=36000):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
    
def get_user_id_from_header():
   
    token = request.headers.get('Authorization')
    if not token:
        raise ValueError("Token is missing!")  
    if token.startswith('Bearer '):
        token = token[7:]  
    try:
        decoded = decode_jwt(token)
        user_id = decoded.get('userid') 
        
        if not user_id:
            raise ValueError("User ID not found in token.")
        
        return user_id
    except ValueError as e:
        raise ValueError(f"Error decoding token: {str(e)}")
