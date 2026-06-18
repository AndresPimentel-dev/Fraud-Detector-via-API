from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, hashed_password:str) -> Optional[User]:
        pass
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass

class PasswordHasher(ABC):
    @abstractmethod
    def get_password_hash(self, password:str ) -> str:
        pass
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str):
        pass

class TokenService(ABC):
    @abstractmethod
    def create_token(self, data: dict) -> str:
        pass
    @abstractmethod
    def verify_token(self, token: str) -> Optional[dict]:
        pass

class PredictionService(ABC):
    @abstractmethod
    def get_contracts(self, company_description: str):
        pass
    @abstractmethod
    def get_prediction(self, contract_name : str, user_budget: float):
        pass