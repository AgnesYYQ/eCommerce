from fastapi.testclient import TestClient
from stripe_async import app
import json

def test_stripe_webhook():
    client = TestClient(app)
    event = {"type": "payment_intent.succeeded", "data": {"object": {"id": "pi_123"}}}
    response = client.post("/stripe/webhook", data=json.dumps(event), headers={"stripe-signature": "test_secret"})
    assert response.status_code == 200
    assert response.json()["status"] == "received"
