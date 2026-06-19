import pytest


def test_register_user(client):
    response = client.post("/register", json={
        "username": "testuser",
        "password": "word"
    })
    assert response.status_code == 201
    assert response.json() == {"STATUS": "creado"}

def test_login_user(client):
    client.post("/register", json={
        "username": "testuser",
        "password": "securepassword"})
    
    response = client.post("/login" , data={"username": "testuser", "password": "securepassword"})

    assert response.status_code ==200
    token = response.json()["token"]
    assert token is not None

def test_prediction(client):
    client.post("/register", json={"username": "testuser", "password": "securepassword"})
    tokendecode = client.post("/login" , data={"username": "testuser", "password": "securepassword"})
    token = tokendecode.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response =  client.post("/obtenercontratos", json={"company_description": "empresa de software"}, headers=headers)
    print(f"JSON BODY: {response.json()}")
    assert response.status_code == 200

def test_price_prediction(client):
    client.post("/register", json={"username": "testuser", "password": "securepassword"})
    tokendecode = client.post("/login" , data={"username": "testuser", "password": "securepassword"})
    token = tokendecode.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response =  client.post("/obtenerprediccion", json={"contract_name":"construccion", "user_budget":"30000000"}, headers=headers)
    print(f"JSON BODY: {response.json()}")
    assert response.status_code == 200