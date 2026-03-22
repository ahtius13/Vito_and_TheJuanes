from fastapi import APIRouter
import json
import os
import joblib
import numpy as np

from app.functions import preprocess_house_features
from models.generator import generate_description

router = APIRouter()

MODEL_PATH = "models/price_model.pkl"
DATA_PATH = "data/houses.json"

model = joblib.load(MODEL_PATH)


@router.post("/houses")
def create_house(house: dict):
    try:
        features = preprocess_house_features(house)

        features_array = np.array(features).reshape(1, -1)

        predicted_price = int(model.predict(features_array)[0])

        description = generate_description(house, predicted_price)

        house_data = house.copy()
        house_data["price"] = predicted_price
        house_data["description"] = description

        if not os.path.exists(DATA_PATH):
            with open(DATA_PATH, "w") as f:
                json.dump([], f)

        with open(DATA_PATH, "r") as f:
            data = json.load(f)

        data.append(house_data)

        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=4)

        return house_data

    except Exception as e:
        return {"error": str(e)}