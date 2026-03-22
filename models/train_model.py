import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "housing.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "price_model.pkl")

data = pd.read_csv(DATA_PATH)

# Convertir yes/no a 1/0
binary_columns = [
    "mainroad", "guestroom", "basement",
    "hotwaterheating", "airconditioning", "prefarea"
]

for col in binary_columns:
    data[col] = data[col].map({"yes": 1, "no": 0})

# Convertir furnishingstatus
data["furnishingstatus"] = data["furnishingstatus"].map({
    "furnished": 2,
    "semi-furnished": 1,
    "unfurnished": 0
})

# Variables
X = data.drop("price", axis=1)
y = data["price"]

# División
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, MODEL_PATH)

print("Modelo entrenado y guardado correctamente en:", MODEL_PATH)