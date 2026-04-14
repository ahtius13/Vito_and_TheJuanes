import pandas as pd

FEATURE_COLUMNS = [
    "area",
    "bedrooms",
    "bathrooms",
    "stories",
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "parking",
    "prefarea",
    "furnishingstatus"
]

def preprocess_house_features(house):
    """
    Convierte los datos del schema en un diccionario ordenado
    exactamente como espera el modelo de Machine Learning
    """

    return {
        "area": house.area,
        "bedrooms": house.bedrooms,
        "bathrooms": house.bathrooms,
        "stories": house.stories,
        "mainroad": house.mainroad,
        "guestroom": house.guestroom,
        "basement": house.basement,
        "hotwaterheating": house.hotwaterheating,
        "airconditioning": house.airconditioning,
        "parking": house.parking,
        "prefarea": house.prefarea,
        "furnishingstatus": house.furnishingstatus
    }


def features_to_dataframe(features_dict):
    """
    Convierte el diccionario de features en un DataFrame
    asegurando el orden correcto de columnas
    """

    df = pd.DataFrame([features_dict])

    df = df[FEATURE_COLUMNS]

    return df


def validate_binary_fields(features_dict):
    """
    Valida que los campos binarios solo tengan valores 0 o 1 = 0 no / 1 yes
    """

    binary_fields = [
        "mainroad",
        "guestroom",
        "basement",
        "hotwaterheating",
        "airconditioning",
        "prefarea"
    ]

    for field in binary_fields:
        value = features_dict[field]
        if value not in [0, 1]:
            raise ValueError(f"El campo '{field}' debe ser 0 o 1")

    return True


def validate_furnishing_status(value):
    """
    Valida el campo furnishing = 0 Sin Amueblar / 1 Semi Amueblado / 2 Amueblado
    """

    if value not in [0, 1, 2]:
        raise ValueError(
            "furnishingstatus debe ser: 0 (unfurnished), 1 (semi-furnished), 2 (furnished)"
        )

    return True