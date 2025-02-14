from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_qr_valid_url():
    response = client.post("/generate_qr", json={"url": "https://www.example.com"})
    assert response.status_code == 200
    assert "qr_code" in response.json()

def test_generate_qr_invalid_url():
    response = client.post("/generate_qr", json={"url": "invalid-url"})
    assert response.status_code == 422  # Unprocessable Entity

def test_generate_qr_missing_url():
    response = client.post("/generate_qr", json={})
    assert response.status_code == 422  # Missing required field
