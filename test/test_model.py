import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join("models", "price_model.pkl")


def test_model_loads():
    model = joblib.load(MODEL_PATH)
    assert model is not None


def test_model_predict_shape():
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([{
        "area": 1000,
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "mainroad": 1,
        "guestroom": 0,
        "basement": 1,
        "hotwaterheating": 0,
        "airconditioning": 1,
        "parking": 2,
        "prefarea": 1,
        "furnishingstatus": 2
    }])

    pred = model.predict(df)

    assert len(pred) == 1
    assert pred[0] > 0