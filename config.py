import secrets
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def generate_secret_key():
    raw_key = secrets.token_urlsafe(32)
    # raw_key = secrets.token_hex(16)
    return raw_key

class Config:
    SECRET_KEY = generate_secret_key()
    print(f"Generated secret key: {SECRET_KEY}")
