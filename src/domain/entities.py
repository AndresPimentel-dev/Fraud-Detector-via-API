from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    username: str
    hashed_password : str

@dataclass
class ContractChooserImput:
    cmp_description: str

@dataclass
class BudgetPrdtImput:
    contract_name: str
    user_budget: float