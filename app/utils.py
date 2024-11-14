from passlib.context import CryptContext

#Telling paslib, what is the default hashing algorithm we want to use
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hash_string(content: str):
    return pwd_context.hash(content)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
