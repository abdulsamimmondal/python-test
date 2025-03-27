import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask App!" in response.data

def test_posts(client):
    """Test the posts route."""
    response = client.get('/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list) 
