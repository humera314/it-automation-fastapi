from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello! The system is healthy ✅"}

def test_check_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "status" in response.json()
