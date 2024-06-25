# portal/utils.py
# ???

import bcrypt
import json
import os

PASSWORD_FILE = 'passwords.json'

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'w') as file:
            json.dump({"passwords": {}}, file)
    with open(PASSWORD_FILE, 'r') as file:
        return json.load(file)

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def add_password(email, password):
    passwords = load_passwords()
    hashed = hash_password(password)
    passwords["passwords"][email] = hashed
    save_passwords(passwords)

def get_password(email):
    passwords = load_passwords()
    return passwords["passwords"].get(email)
