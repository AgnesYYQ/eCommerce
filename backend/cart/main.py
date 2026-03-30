from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

carts = {}

class CartItem(BaseModel):
    product_id: int
    quantity: int

@app.get("/cart/{user_id}", response_model=List[CartItem])
def get_cart(user_id: str):
    return carts.get(user_id, [])

@app.post("/cart/{user_id}", response_model=List[CartItem])
def add_to_cart(user_id: str, item: CartItem):
    if user_id not in carts:
        carts[user_id] = []
    carts[user_id].append(item)
    return carts[user_id]
