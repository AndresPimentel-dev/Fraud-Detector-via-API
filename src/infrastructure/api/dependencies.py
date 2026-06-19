from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy.orm import Session
import os


from src.use_cases.user_cases import UserCases
from src.use_cases.prediction_cases import PredictionUseCase
from src.infrastructure.database.repositories import UserRepository
from src.infrastructure.security.password_jwt import HashProvider, TokenServices
from src.infrastructure.database.connection import get_db
from src.infrastructure.api.routes import oauth2_scheme
from src.infrastructure.models.MLrepository import PredictionProvider

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE = 30

TOKEN = str

def get_auth_case(db: Session = Depends(get_db)) -> UserCases:
    return UserCases(UserRepository(db), HashProvider(), TokenServices(secret_key=SECRET_KEY, algorithm= ALGORITHM, expire_time= ACCESS_TOKEN_EXPIRE))  

def get_token_use() -> TOKEN:
    return TokenServices(secret_key=SECRET_KEY, algorithm= ALGORITHM, expire_time= ACCESS_TOKEN_EXPIRE)
    
def get_currrent_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    hola = TokenServices(SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE)
    decode = hola.verify_token(token)
    if not decode:
        return None
    repo = UserRepository(db)
    username = repo.get_by_username(decode)
    if not username:
        return None
    return username

def get_predictions_case() -> PredictionUseCase:
    return PredictionUseCase(PredictionProvider())