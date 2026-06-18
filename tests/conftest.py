import pytest
from fastapi.testclient import TestClient

# Importamos la aplicación y las dependencias reales para poder sobrescribirlas
from src.infrastructure.api.main import app 
from src.infrastructure.api.dependencies import (
    get_auth_case, 
    get_token_use, 
    get_currrent_user, 
    get_predictions_case
)

# ==========================================
# IMPLEMENTACIONES FALSAS (MOCKS)
# ==========================================

class MockUserCases:
    def register_user(self, username, password):
        return "fake_registered_token"
    
    def login_user(self, username, password):
        class FakeUser:
            username = "testuser"
            hashed_password = "fake_hashed_password"
        return FakeUser()

class MockTokenServices:
    def create_token(self, data):
        return "fake_access_token"

class MockPredictionUseCase:
    def get_contracts(self, cp_dst: str):
        return [
            {
                "nombre_del_procedimiento": "Contrato Falso de Prueba", 
                "precio_base": 150000.0, 
                "similaridad": 0.92
            }
        ]
    
    def get_prediction(self, contract_name: str, user_budget: float):
        return {
            "status": "success",
            "data": {
                "probability": 0.85,
                "base_price": 150000.0,
                "user_budget": user_budget
            }
        }

# ==========================================
# FIXTURES DE PYTEST
# ==========================================

@pytest.fixture(scope="module", autouse=True)
def setup_dependency_overrides():
    """
    Este fixture se ejecuta automáticamente. Configura los overrides de FastAPI
    antes de los tests y los limpia por completo al finalizar.
    """
    class AuthenticatedUser:
        username = "testuser"

    # Aplicamos los reemplazos en el diccionario de FastAPI
    app.dependency_overrides[get_auth_case] = lambda: MockUserCases()
    app.dependency_overrides[get_token_use] = lambda: MockTokenServices()
    app.dependency_overrides[get_currrent_user] = lambda: AuthenticatedUser()
    app.dependency_overrides[get_predictions_case] = lambda: MockPredictionUseCase()
    
    yield # Aquí es donde se ejecutan los tests
    
    # Limpieza: restablece las dependencias originales de la app
    app.dependency_overrides.clear()


@pytest.fixture(scope="module")
def client():
    """Proporciona el TestClient de FastAPI para realizar las peticiones HTTP."""
    with TestClient(app) as test_client:
        yield test_client