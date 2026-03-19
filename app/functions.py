import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "price_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_price(house_data):
    """
    Recibe un diccionario con los datos de la casa y devuelve el precio estimado
    """
    features = ["area", "bedrooms", "bathrooms", "stories", "parking"]
    df = pd.DataFrame([{k: house_data[k] for k in features}])
    prediction = model.predict(df)
    return int(prediction[0])