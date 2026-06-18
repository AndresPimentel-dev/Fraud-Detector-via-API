from typing import Optional

from src.domain.entities import BudgetPrdtImput, ContractChooserImput
from src.domain.interfaces import PredictionService

class PredictionUseCase:
    def __init__(self, repo: PredictionService):
        self.repo = repo

    def get_contracts(self, cp_dst: str):
        contracts = self.repo.get_contracts(cp_dst)
        return contracts
    
    def get_prediction(self, contract_name: str, user_budget: float):
        prediction = self.repo.get_prediction(contract_name, user_budget)
        return prediction