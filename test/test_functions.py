import pytest
import pandas as pd

from app.functions import (
    preprocess_house_features,
    features_to_dataframe,
    validate_binary_fields,
    validate_furnishing_status,
    FEATURE_COLUMNS
)

from app.schemas import HouseInput


@pytest.fixture
def sample_house():
    return HouseInput(
        area=2000,
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


def test_preprocess_house_features(sample_house):
    features = preprocess_house_features(sample_house)

    assert isinstance(features, dict)
    assert set(features.keys()) == set(FEATURE_COLUMNS)
    assert features["area"] == 2000
    assert features["bedrooms"] == 3


def test_features_to_dataframe(sample_house):
    features = preprocess_house_features(sample_house)
    df = features_to_dataframe(features)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, len(FEATURE_COLUMNS))
    assert list(df.columns) == FEATURE_COLUMNS


def test_validate_binary_fields_valid(sample_house):
    features = preprocess_house_features(sample_house)
    assert validate_binary_fields(features) is True


def test_validate_binary_fields_invalid(sample_house):
    features = preprocess_house_features(sample_house)
    features["mainroad"] = 2

    with pytest.raises(ValueError):
        validate_binary_fields(features)


def test_validate_furnishing_status_valid():
    assert validate_furnishing_status(0) is True
    assert validate_furnishing_status(1) is True
    assert validate_furnishing_status(2) is True


def test_validate_furnishing_status_invalid():
    with pytest.raises(ValueError):
        validate_furnishing_status(99)


def test_full_preprocess_pipeline(sample_house):
    features = preprocess_house_features(sample_house)

    validate_binary_fields(features)
    validate_furnishing_status(features["furnishingstatus"])

    df = features_to_dataframe(features)

    assert df.iloc[0]["area"] == 2000
    assert df.iloc[0]["parking"] == 2