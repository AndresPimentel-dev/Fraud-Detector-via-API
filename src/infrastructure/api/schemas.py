from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    token: str
    token_type: str

class ContractChooserImput(BaseModel):
    company_description: str

class BudgetPredictorImput(BaseModel):
    contract_name: str
    user_budget: float