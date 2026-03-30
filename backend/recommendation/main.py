from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RecommendationRequest(BaseModel):
    user_id: str

class ProductRecommendation(BaseModel):
    product_id: int
    score: float

@app.post("/recommend", response_model=List[ProductRecommendation])
def recommend_products(req: RecommendationRequest):
    # Simulate recommendations
    return [ProductRecommendation(product_id=1, score=0.9), ProductRecommendation(product_id=2, score=0.8)]
