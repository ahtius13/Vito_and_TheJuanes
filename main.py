from fastapi import FastAPI
from app.functions import predict_price
from pydantic import BaseModel

class HouseInput(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Housing API running"}

@app.post("/predict")
def predict(house: HouseInput):
    price = predict_price(house.dict())
    return {"estimated_price": price}