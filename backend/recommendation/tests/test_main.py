from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recommend_products():
    response = client.post("/recommend", json={"user_id": "test"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
