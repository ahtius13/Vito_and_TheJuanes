# app/routes/get_houses.py

from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

@router.get("/houses")
def get_houses():
    data_file = "data/houses.json"

    if not os.path.exists(data_file):
        return []

    try:
        with open(data_file, "r", encoding="utf-8") as f:
            houses = json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error al leer el archivo de viviendas.")

    return houses