from typing import Optional

from src.domain.entities import User
from src.domain.interfaces import UserRepositoryInterface, PasswordHasher, TokenService


class UserCases:
    def __init__(self, user_repo: UserRepositoryInterface, pwd_hs: PasswordHasher, tk_ct: TokenService):
        self.user_repo = user_repo
        self.pwd_hs = pwd_hs
        self.tk_ct = tk_ct

    def register_user(self, username:str, password:str) -> Optional[User]:
        existing_username = self.user_repo.get_by_username(username=username)
        if existing_username:
            return None
        hashed_password = self.pwd_hs.get_password_hash(password=password)
        new_user = User(None, username, hashed_password)
        self.user_repo.create_user(new_user)
        return self.tk_ct.create_token(data={"sub": new_user.username})
    
    def login_user(self, username:str, password:str):
        user = self.user_repo.get_by_username(username=username)
        if not user:
            return None
        if not self.pwd_hs.verify_password(plain_password=password, hashed_password=user.hashed_password):
            return None
        return self.tk_ct.create_token(data={"sub": user.username})