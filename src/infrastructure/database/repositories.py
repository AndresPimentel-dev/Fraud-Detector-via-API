from typing import Optional
from sqlalchemy.orm import Session

from src.domain.entities import User
from src.domain.interfaces import UserRepositoryInterface
from src.infrastructure.database.models import UsersTable

class UserRepository(UserRepositoryInterface):
    def __init__(self, db=Session):
        self.db = db

    def get_by_username(self, username):
        db_user = self.db.query(UsersTable).filter(username == UsersTable.username).first()
        if not db_user:
            return None
        return db_user
    def create_user(self, username, hashed_password):
        new_user = UsersTable(username= username, hashed_password=hashed_password)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user