from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import hmac
import hashlib
import os
import json

app = FastAPI()

STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "test_secret")

@app.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")
    # In production, use stripe.Webhook.construct_event for verification
    # Here, we just simulate verification
    if not hmac.compare_digest(sig_header, STRIPE_WEBHOOK_SECRET):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Invalid signature"})
    event = json.loads(payload)
    # Simulate putting event into SQS (replace with boto3 in production)
    print(f"Received Stripe event: {event}")
    return {"status": "received"}
