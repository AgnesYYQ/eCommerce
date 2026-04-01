from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_track_event():
    response = client.post("/event", json={"user_id": "test", "event_type": "view", "metadata": {}})
    assert response.status_code == 200
    assert response.json()["status"] == "tracked"
