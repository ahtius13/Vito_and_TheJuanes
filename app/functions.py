import json
import os

DATA_FILE = os.path.join("data", "houses.json")


def yes_no_to_binary(value):
    """
    Convierte 'yes' a 1 y 'no' a 0.
    """
    if isinstance(value, str):
        value = value.lower()
        if value == "yes":
            return 1
        elif value == "no":
            return 0
    return value 


def preprocess_house_features(data: dict):
    return [
        data["area"],
        data["bedrooms"],
        data["bathrooms"],
        data["stories"],
        data["mainroad"],
        data["guestroom"],
        data["basement"],
        data["hotwaterheating"],
        data["airconditioning"],
        data["parking"],
        data["prefarea"],
        data["furnishingstatus"]
    ]


def load_houses():
    """
    Carga todas las viviendas desde houses.json
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            houses = json.load(f)
        except json.JSONDecodeError:
            houses = []
    return houses


def save_house(house):
    """
    Guarda una vivienda nueva en houses.json
    """
    houses = load_houses()
    houses.append(house)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(houses, f, ensure_ascii=False, indent=4)
    return house