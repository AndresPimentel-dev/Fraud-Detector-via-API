import pytest

def test_register_endpoint(client):
    """Prueba el endpoint de registro de usuarios."""
    payload = {
        "username": "newuser",
        "password": "securepassword123"
    }
    response = client.post("/register", json=payload)
    
    assert response.status_code == 201
    assert response.json() == {"STATUS": "creado"}


def test_login_endpoint(client):
    """Prueba el endpoint de inicio de sesión usando Form Data."""
    form_data = {
        "username": "testuser",
        "password": "correctpassword"
    }
    response = client.post("/login", data=form_data)
    
    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_obtener_contratos_endpoint(client):
    """Prueba el recomendador de contratos NLP asegurado."""
    headers = {"Authorization": "Bearer fake_access_token"}
    payload = {
        "company_description": "Desarrollo de software"
    }
    # Pasamos los headers en la petición
    response = client.post("/obtenercontratos", json=payload, headers=headers)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obtener_prediccion_endpoint(client):
    """Prueba la predicción asegurada."""
    headers = {"Authorization": "Bearer fake_access_token"}
    payload = {
        "contract_name": "construccion",
        "user_budget": 130000.0
    }
    response = client.post("/obtenerprediccion", json=payload, headers=headers)
    
    assert response.status_code == 200
    assert response.json()["status"] == "success"