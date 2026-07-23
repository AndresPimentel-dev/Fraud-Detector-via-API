import pytest


def test_register_user(client):
    response = client.post("/register", json={
        "username": "testuser",
        "password": "word"
    })
    assert response.status_code == 201
    assert response.json() == {"STATUS": "creado"}

#def test_login_user(client):
#    client.post("/register", json={
#        "username": "testuser",
#        "password": "securepassword"})
#    
#    response = client.post("/login" , data={"username": "testuser", "password": "securepassword"})
#
#    assert response.status_code ==200
#    token = response.json()["token"]
#    assert token is not None
#
#def test_prediction(client):
#    client.post("/register", json={"username": "testuser", "password": "securepassword"})
#    tokendecode = client.post("/login" , data={"username": "testuser", "password": "securepassword"})
#    token = tokendecode.json()["token"]
#    headers = {"Authorization": f"Bearer {token}"}
#
#    response =  client.post("/obtenercontratos", json={
#  "Time": 0.0,
#  "V1": -1.3598,
#  "V2": -0.0727,
#  "V3": 2.5363,
#  "V4": 1.3781,
#  "V5": -0.3383,
#  "V6": 0.4623,
#  "V7": 0.2395,
#  "V8": 0.0986,
#  "V9": 0.3637,
#  "V10": 0.0907,
#  "V11": -0.5515,
#  "V12": -0.6178,
#  "V13": -0.9913,
#  "V14": -0.3111,
#  "V15": 1.4681,
#  "V16": -0.4704,
#  "V17": 0.2079,
#  "V18": 0.0257,
#  "V19": 0.4039,
#  "V20": 0.2514,
#  "V21": -0.0183,
#  "V22": 0.2778,
#  "V23": -0.1104,
#  "V24": 0.0669,
#  "V25": 0.1285,
#  "V26": -0.1891,
#  "V27": 0.1335,
#  "V28": -0.0210,
#  "Amount": 149.62
#}, headers=headers)
#    print(f"JSON BODY: {response.json()}")
#    assert response.status_code == 200