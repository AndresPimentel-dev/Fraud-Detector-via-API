from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

from src.infrastructure.api.schemas import UserCreate, ContractChooserImput, BudgetPredictorImput, TokenResponse
from src.use_cases.user_cases import UserCases
from src.use_cases.prediction_cases import PredictionUseCase
from src.infrastructure.database.connection import get_db
from src.infrastructure.models.MLrepository import PredictionProvider
from src.domain.entities import User
from src.infrastructure.database.repositories import UserRepository
from src.infrastructure.security.password_jwt import TokenServices
from src.infrastructure.api.dependencies import get_auth_case, get_token_use, get_currrent_user, get_predictions_case

router = APIRouter()



#endpoints de login y register

@router.post("/register",  status_code=201)
def register(user: UserCreate, auth_case: UserCases = Depends(get_auth_case)):
    new_user = auth_case.register_user(user.username, user.password)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already exists")
    return {"STATUS": "creado"}

@router.post("/login", response_model=TokenResponse, status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), auth_use_case: UserCases = Depends(get_auth_case), token_use: TokenServices = Depends(get_token_use)):

    user = auth_use_case.login_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="INCORRECT")
    token = token_use.create_token(data= {"sub": form_data.username})
    return {"token": token, "token_type": "bearer"}



#endpoints de prediccion

@router.post("/obtenercontratos", status_code=200)
def prediction_contracs(data:ContractChooserImput, current_user: User = Depends(get_currrent_user), predict_case: PredictionUseCase = Depends(get_predictions_case)):
    return predict_case.get_contracts(data.company_description)

@router.post("/obtenerprediccion", status_code=200)
def prediction(data: BudgetPredictorImput, current_user: User = Depends(get_currrent_user), predict_case: PredictionUseCase = Depends(get_predictions_case)):
    return predict_case.get_prediction(data.contract_name, data.user_budget)

