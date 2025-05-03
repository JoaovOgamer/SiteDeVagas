import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password_attempt, stored_hash):
    return bcrypt.checkpw(password_attempt.encode(), stored_hash.encode('utf-8'))