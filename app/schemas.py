from pydantic import BaseModel, Field, field_validator


class HouseInput(BaseModel):
    area: int = Field(..., example=1000)
    bedrooms: int
    bathrooms: int
    stories: int

    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int

    parking: int
    prefarea: int

    furnishingstatus: int = Field(..., example=2)

    @field_validator("furnishingstatus")
    @classmethod
    def validate_furnishingstatus(cls, v):
        if v not in (0, 1, 2):
            raise ValueError("furnishingstatus must be 0, 1 or 2")
        return v