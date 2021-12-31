from passlib.context import CryptContext # hash = password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # hash = al/gr

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)