import pytest
from unittest.mock import patch

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


@patch("models.generator.generator")
def test_generate_description(mock_generator, sample_house):
    mock_generator.return_value = [{
        "generated_text": (
            "Se ofrece en venta una excelente vivienda de 1500 m², "
            "con 3 habitaciones y 2 baños. Excelente iluminación natural."
        )
    }]

    price = 300000

    description = generate_description(sample_house, price)

    assert isinstance(description, str)
    assert len(description) > 20

    # Verifica que usa datos del input
    assert "1500" in description
    assert "3" in description

    # Verifica que incluye precio
    assert "300000" in description