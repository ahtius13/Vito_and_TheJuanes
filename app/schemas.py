from pydantic import BaseModel, Field


class HouseInput(BaseModel):
    area: int = Field(..., example=1000, description="Superficie en metros cuadrados")
    bedrooms: int = Field(..., example=1, description="Número de habitaciones")
    bathrooms: int = Field(..., example=1, description="Número de baños")
    stories: int = Field(..., example=1, description="Número de plantas")

    mainroad: int = Field(..., example=1, description="En la carretera principal 1 = sí, 0 = no")
    guestroom: int = Field(..., example=1, description="Habitacion de huesped 1 = sí, 0 = no")
    basement: int = Field(..., example=1, description="Sotano 1 = sí, 0 = no")
    hotwaterheating: int = Field(..., example=1, description="Calentador de agua 1 = sí, 0 = no")
    airconditioning: int = Field(..., example=1, description="Aire acondicionado 1 = sí, 0 = no")

    parking: int = Field(..., example=1, description="Número de plazas de aparcamiento")
    prefarea: int = Field(..., example=1, description="1 = zona preferente, 0 = no")

    furnishingstatus: int = Field(
        ...,
        example=2,
        description="0 = sin amueblar, 1 = semi amueblada, 2 = amueblada"
    )