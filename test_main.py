import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/task", json={"title": "Test Task", "description": "Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"