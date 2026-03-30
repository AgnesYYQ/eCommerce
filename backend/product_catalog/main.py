from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory product store (replace with DB integration)
products = []

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: int

@app.get("/products", response_model=List[Product])
def list_products():
    return products

@app.post("/products", response_model=Product)
def add_product(product: Product):
    products.append(product)
    return product

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
