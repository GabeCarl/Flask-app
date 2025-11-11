import os
import requests

url=os.getenv("URL")

def test_health():
    response = requests.get(f"{url}/health")
    assert response.status_code == 200

def test_users_get():
    response = requests.get(f"{url}/users")
    assert response.status_code == 200

def test_users_post():
    response = requests.post(f"{url}/users", json={"nome": "Teste"})
    assert response.status_code == 201