import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "housing.csv")

data = pd.read_csv(DATA_PATH)

features = ["area", "bedrooms", "bathrooms", "stories", "parking"]
X = data[features]
y = data["price"]

model = RandomForestRegressor()

model.fit(X, y)

if not os.path.exists(os.path.join(BASE_DIR, "models")):
    os.makedirs(os.path.join(BASE_DIR, "models"))

joblib.dump(model, os.path.join(BASE_DIR, "models", "price_model.pkl"))

print("Modelo entrenado y guardado en models/price_model.pkl")