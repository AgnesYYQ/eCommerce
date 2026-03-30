from fastapi import FastAPI, Request, status, BackgroundTasks
from fastapi.responses import JSONResponse
import hmac
import hashlib
import os
import json
import boto3

app = FastAPI()

STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "test_secret")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/123456789012/payment-events")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

sqs = boto3.client("sqs", region_name=AWS_REGION)

@app.post("/stripe/webhook")
async def stripe_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")
    # In production, use stripe.Webhook.construct_event for verification
    if not hmac.compare_digest(sig_header, STRIPE_WEBHOOK_SECRET):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Invalid signature"})
    event = json.loads(payload)
    # Immediately enqueue event to SQS for async processing
    background_tasks.add_task(send_to_sqs, event)
    return {"status": "received"}

def send_to_sqs(event):
    sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody=json.dumps(event))

# Multi-region: Use environment variable or config to select region/queue
# For failover, deploy this service in each region and point SQS_QUEUE_URL to the local region's queue
