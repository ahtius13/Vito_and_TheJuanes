from fastapi.testclient import TestClient
from main import app 


client = TestClient(app)


def test_get_houses():
    response = client.get("/houses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_houses():
    response = client.get("/houses/filter?min_price=100000&max_price=9999999")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_house():
    payload = {
        "area": 1200,
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "mainroad": 1,
        "guestroom": 0,
        "basement": 1,
        "hotwaterheating": 0,
        "airconditioning": 1,
        "parking": 2,
        "prefarea": 1,
        "furnishingstatus": 2
    }

    response = client.post("/houses", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "price" in data
    assert "description" in data