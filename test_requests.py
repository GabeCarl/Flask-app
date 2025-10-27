import pytest
import requests

url = "http://127.0.0.1:5000"

def test_health_check():
    response = requests.get(f"{url}/health")
    print (response.text)
    assert response.status_code == 200

def test_get_users():
    response = requests.get(f"{url}/users")
    print (response.text)
    assert response.status_code == 200

def test_post_user():
    payload = {"nome": "Teste"}
    response = requests.post(f"{url}/users", json=payload)
    print (response.text)
    assert response.status_code == 201