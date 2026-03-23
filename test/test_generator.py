import pytest
from app.schemas import HouseInput
from models.generator import generate_description


@pytest.fixture
def sample_house():
    return HouseInput(
        area=1500,
        bedrooms=3,
        bathrooms=2,
        stories=2,
        mainroad=1,
        guestroom=1,
        basement=1,
        hotwaterheating=0,
        airconditioning=1,
        parking=1,
        prefarea=1,
        furnishingstatus=1
    )


def test_generate_description(sample_house):
    price = 300000

    description = generate_description(sample_house, price)

    assert isinstance(description, str)
    assert len(description) > 20  # mínimo razonable
    assert "1500" in description  # usa datos
    assert "3" in description     # usa habitaciones