from fastapi import APIRouter, Query
import pandas as pd
import os

router = APIRouter()

DATA_PATH = os.path.join("data", "houses.csv")


@router.get("/houses/filter")
def filter_houses(
    min_price: int = Query(None, description="Precio mínimo"),
    max_price: int = Query(None, description="Precio máximo")
):

    if not os.path.exists(DATA_PATH):
        return {"message": "No hay casas registradas"}

    df = pd.read_csv(DATA_PATH)

    if df.empty:
        return {"message": "No hay casas registradas"}

    # Filtro por precio mínimo
    if min_price is not None:
        df = df[df["price"] >= min_price]

    # Filtro por precio máximo
    if max_price is not None:
        df = df[df["price"] <= max_price]

    # Ordenar (de mayor a menor por defecto)
    df = df.sort_values(by="price", ascending=False)

    return df.to_dict(orient="records")