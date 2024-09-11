import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"

def test_create_item_valid_data():
    data = {
        "name": "Телефон",
        "price": 40000,
        "sellerID": 220315
    }
    response = requests.post(f"{BASE_URL}/item", json=data)
    
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_item_invalid_seller_id_too_low():
    data = {
        "name": "Телефон",
        "price": 85566,
        "sellerID": 111110
    }
    response = requests.post(f"{BASE_URL}/item", json=data)

    assert response.status_code == 400
    assert response.json()["status"] == "не передан"

def test_create_item_invalid_seller_id_too_high():
    data = {
        "name": "Фотоаппарат",
        "price": 30000,
        "sellerID": 1000000
    }
    response = requests.post(f"{BASE_URL}/item", json=data)

    assert response.status_code == 400
    assert response.json()["status"] == "не передан"

def test_create_item_missing_required_field():
    data = {
        "name": "Телефон",
        "price": 85566,
        "sellerID": ""
    }
    response = requests.post(f"{BASE_URL}/item", json=data)

    assert response.status_code == 400
    assert response.json()["status"] == "не передан"

def test_get_item_by_valid_id():
    valid_id = "a342fe83-4907-43e9-8c8d-9e8304812a58"
    response = requests.get(f"{BASE_URL}/item/{valid_id}")

    assert response.status_code == 200
    assert "name" in response.json()
    assert "price" in response.json()
    assert "sellerID" in response.json()

def test_get_item_by_invalid_id():
    invalid_id = "a342fe83-4907-43e9-8c8d-9e8304812"
    response = requests.get(f"{BASE_URL}/item/{invalid_id}")

    assert response.status_code == 404
    assert "error" in response.json()
    assert response.json()["error"] == "item not found"

def test_get_items_by_valid_seller_id():
    seller_id = 220315
    response = requests.get(f"{BASE_URL}/{seller_id}/item")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_items_by_invalid_seller_id():
    invalid_seller_id = 11111223
    response = requests.get(f"{BASE_URL}/{invalid_seller_id}/item")

    assert response.status_code == 200
    assert response.json() == []