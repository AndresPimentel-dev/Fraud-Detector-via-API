import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

from src.domain.interfaces import PredictionService

current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Unir la ruta con el nombre del archivo (están juntos)
model_path = os.path.join(current_dir, 'modelo_fraude.pkl')
        

##################################################################

class PredictionProvider(PredictionService):
    def __init__(self):
        self.model = joblib.load(model_path)
    
    def get_prediction(self, transaccion: dict):
        # Convertir el diccionario en un DataFrame de pandas
        df = pd.DataFrame([transaccion])
        
        # Asegurarse de que las columnas estén en el mismo orden que durante el entrenamiento

        
        # Realizar la predicción utilizando el modelo cargado
        prediction = self.model.predict(df)
        
        return {"fraude": bool(prediction[0])}