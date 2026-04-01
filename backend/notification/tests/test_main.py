from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_send_notification():
    response = client.post("/notify", json={"user_id": "test", "message": "Hello"})
    assert response.status_code == 200
    assert response.json()["status"] == "sent"
