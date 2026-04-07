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
def test_generate_description_mock(mock_pipeline, sample_house):
    mock_pipeline.return_value = [{
        "generated_text": "Se ofrece en venta una excelente vivienda de 1500 m²... Excelente iluminación natural."
    }]

    price = 300000

    description = generate_description(sample_house, price)

    assert isinstance(description, str)
    assert "1500" in description
    assert "3" in description
    assert "300000" in description