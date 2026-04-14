from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()

DATA_PATH = os.path.join("data", "houses.csv")


@router.get("/houses")
def get_houses():

    if not os.path.exists(DATA_PATH):
        return {"message": "No hay casas registradas"}

    df = pd.read_csv(DATA_PATH)

    if df.empty:
        return {"message": "No hay casas registradas"}

    return df.to_dict(orient="records")