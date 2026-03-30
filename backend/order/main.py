from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

orders = []

class Order(BaseModel):
    id: int
    user_id: str
    items: list
    total: float

@app.get("/orders", response_model=List[Order])
def list_orders():
    return orders

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    orders.append(order)
    return order
