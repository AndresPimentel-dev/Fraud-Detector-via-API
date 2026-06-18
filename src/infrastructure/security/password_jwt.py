import jwt
import bcrypt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends
from passlib.context import CryptContext
from datetime import timedelta, datetime
from typing import Optional
from src.domain.interfaces import PasswordHasher, TokenService



class HashProvider(PasswordHasher):
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    def get_password_hash(self, plain_password: str):
        return self.pwd_context.hash(plain_password)
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
    

    
class TokenServices(TokenService):
    def __init__(self, secret_key, algorithm, expire_time):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expire_time = expire_time
    def create_token(self, data: dict, expires_delta: Optional[timedelta] =None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self.expire_time)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, self.algorithm)
    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username = payload.get("sub")
            if username is None:
                return None
            return username
        except InvalidTokenError:
            return None