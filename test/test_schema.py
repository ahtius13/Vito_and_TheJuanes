import pytest
from pydantic import ValidationError

from app.schemas import HouseInput


def test_house_input_valid():
    house = HouseInput(
        area=1000,
        bedrooms=3,
        bathrooms=2,
        stories=2,
        mainroad=1,
        guestroom=0,
        basement=1,
        hotwaterheating=0,
        airconditioning=1,
        parking=2,
        prefarea=1,
        furnishingstatus=2
    )

    assert house.area == 1000
    assert house.furnishingstatus in [0, 1, 2]


def test_house_input_invalid_furnishing():
    with pytest.raises(ValidationError):
        HouseInput(
            area=1000,
            bedrooms=3,
            bathrooms=2,
            stories=2,
            mainroad=1,
            guestroom=0,
            basement=1,
            hotwaterheating=0,
            airconditioning=1,
            parking=2,
            prefarea=1,
            furnishingstatus=99
        )