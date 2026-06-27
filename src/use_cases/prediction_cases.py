from typing import Optional

from src.domain.entities import Transaccion
from src.domain.interfaces import PredictionService

class PredictionUseCase:
    def __init__(self, repo: PredictionService):
        self.repo = repo
    
    def get_prediction(self, transaccion: Optional[Transaccion]):
        prediction = self.repo.get_prediction(transaccion)
        return prediction