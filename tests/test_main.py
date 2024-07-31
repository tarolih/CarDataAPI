import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_products():
    response = client.get("/get_products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    for product_id, product in data.items():
        assert "description" in product


def test_get_product_details():
    response = client.get("/get_products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Small Car"

    # Non-existing product
    response = client.get("/get_products/999")
    assert response.status_code == 404


def test_set_price():
    new_price = 9999.99
    response = client.post(f"/set_price/1", json={"price": new_price})
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == new_price

    # Non-existing product
    response = client.post(f"/set_price/999", json={"price": new_price})
    assert response.status_code == 404
