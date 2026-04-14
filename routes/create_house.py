from fastapi import APIRouter
import pandas as pd
import os
import joblib

from app.schemas import HouseInput
from app.functions import preprocess_house_features
from models.generator import generate_description

router = APIRouter()

MODEL_PATH = os.path.join("models", "price_model.pkl")
DATA_PATH = os.path.join("data", "houses.csv")

model = joblib.load(MODEL_PATH)


@router.post("/houses")
def create_house(house: HouseInput):

    # Preprocesar datos
    features = preprocess_house_features(house)

    # Convertir a DataFrame
    df_features = pd.DataFrame([features])

    # Predecir precio
    price = int(model.predict(df_features)[0])

    # Generar descripción
    description = generate_description(house, price)

    # Crear fila completa
    new_row = {
        **features,
        "price": price,
        "description": description
    }

    df_new = pd.DataFrame([new_row])

    if os.path.exists(DATA_PATH):
        df_existing = pd.read_csv(DATA_PATH)
        df_all = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_all = df_new

    df_all.to_csv(DATA_PATH, index=False)

    return new_row