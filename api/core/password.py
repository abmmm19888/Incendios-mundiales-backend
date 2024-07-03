#!/user/bin/env python3

from passlib.context import CryptContext

context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def verify_password(plain_password, hashed_password):
    return context.verify(plain_password, hashed_password)

def hash_password(password):
    return context.hash(password)

