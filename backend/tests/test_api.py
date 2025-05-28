import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

def test_generate_response():
    with patch('models.generate_responses') as mock_generate:
        mock_generate.return_value = ("Casual response", "Formal response")
        
        response = client.post(
            "/generate",
            json={"user_id": "test_user", "query": "test query"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "casual_response" in data
        assert "formal_response" in data
        assert data["casual_response"] == "Casual response"
        assert data["formal_response"] == "Formal response"

def test_get_history():
    response = client.get("/history?user_id=test_user")
    assert response.status_code == 200
    assert "history" in response.json()

def test_invalid_request():
    response = client.post(
        "/generate",
        json={"invalid": "data"}
    )
    assert response.status_code == 422  # Validation error 