from src.app.hello import app 
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check route."""
    response = client.get('/health')
    assert response.status_code == 200

def test_users_get(client):
    """Test the users route."""
    response = client.get('/users')
    assert response.status_code == 200

def test_users_post(client):
    """Test the users post route."""
    response = client.post('/users', json={"nome": "Teste"})
    assert response.status_code == 201
