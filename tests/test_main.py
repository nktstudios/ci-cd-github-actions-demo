from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Github Actions Demo from version 1!"}

def test_sum():
    response = client.get("/sum/2/3")
    assert response.status_code == 200
    assert response.json()["result"] == 5