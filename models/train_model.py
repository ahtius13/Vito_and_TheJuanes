import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "housing.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "price_model.pkl")


def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"No se encontró el dataset en {DATA_PATH}")

    # Leer todo como string para poder limpiar
    df = pd.read_csv(DATA_PATH, dtype=str)

    return df


def clean_numeric_columns(df):
    """
    Corrige columnas numéricas con comas como decimales
    """
    numeric_columns = ["price", "area"]

    for col in numeric_columns:
        df[col] = (
            df[col]
            .str.replace(",", ".", regex=False)  # cambia coma por punto
            .str.replace('"', '', regex=False)   # elimina comillas si existen
            .astype(float)                      # convierte a float
        )

    return df


def preprocess_data(df):
    """
    Convierte columnas categóricas a numéricas
    """
    binary_map = {"yes": 1, "no": 0}

    binary_columns = [
        "mainroad",
        "guestroom",
        "basement",
        "hotwaterheating",
        "airconditioning",
        "prefarea"
    ]

    for col in binary_columns:
        df[col] = df[col].map(binary_map)

    furnishing_map = {
        "unfurnished": 0,
        "semi-furnished": 1,
        "furnished": 2
    }

    df["furnishingstatus"] = df["furnishingstatus"].map(furnishing_map)

    return df


def train_model():
    df = load_data()

    df = clean_numeric_columns(df)

    df = preprocess_data(df)

    # Features y target
    X = df.drop("price", axis=1)
    y = df["price"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Guardar modelo
    joblib.dump(model, MODEL_PATH)

    print(f"Modelo entrenado y guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()