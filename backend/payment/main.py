from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PaymentRequest(BaseModel):
    order_id: int
    amount: float
    method: str

@app.post("/pay")
def process_payment(payment: PaymentRequest):
    # Simulate payment processing
    return {"status": "success", "order_id": payment.order_id}
