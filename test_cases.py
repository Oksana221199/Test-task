import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1/item"

@pytest.fixture
def valid_item_data():
    return {
        "name": "Телефон",
        "price": 40000,


        "sellerID": 220315
    }

@pytest.fixture
def invalid_seller_id_too_low():
    return {
        "name": "Телефон",
        "price": 85566,
        "sellerID": 111110
    }

@pytest.fixture
def invalid_seller_id_too_high():
    return {
        "name": "Фотоаппарат",
        "price": 30000,
        "sellerID": 1000000
    }

@pytest.fixture
def missing_required_field():
    return {
        "name": "Телефон",
        "price": 85566,
        "sellerID": ""
    }

def test_create_item_with_valid_data(valid_item_data):
    response = requests.post(BASE_URL, json=valid_item_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_item_with_invalid_seller_id_too_low(invalid_seller_id_too_low):
    response = requests.post(BASE_URL, json=invalid_seller_id_too_low)
    assert response.status_code == 400
    assert response.json()["status"] == "не передан"

def test_create_item_with_invalid_seller_id_too_high(invalid_seller_id_too_high):
    response = requests.post(BASE_URL, json=invalid_seller_id_too_high)
    assert response.status_code == 400
    assert response.json()["status"] == "не передан"

def test_create_item_with_missing_required_field(missing_required_field):
    response = requests.post(BASE_URL, json=missing_required_field)
    assert response.status_code == 400
    assert response.json()["status"] == "не передан"

@pytest.fixture
def create_valid_item():
    data = {
        "name": "Телефон",
        "price": 40000,
        "sellerID": 220315
    }
    response = requests.post(BASE_URL, json=data)
    assert response.status_code == 200
    return response.json()["id"]

def test_successful_item_retrieval(create_valid_item):
    item_id = create_valid_item
    with requests.get(f"{BASE_URL}/{item_id}") as response:
        assert response.status_code == 200
        response_data = response.json()
        assert_in("name", response_data)
        assert_in("price", response_data)
        assert_in("sellerID", response_data)
        print("item_data:", response_data)

@pytest.mark.parametrize("invalid_id", [
    "a342fe83-4907-43e9-8c8d-9e8304812",
    "invalid_id"
])
def test_unsuccessful_item_retrieval(invalid_id):
    with requests.get(f"{BASE_URL}/{invalid_id}") as response:
        assert response.status_code == 404
        response_data = response.json()
        assert_in("error", response_data)
        assert response_data["error"] == "item not found"


def test_get_items_by_valid_seller_id():
    seller_id = 220315
    with requests.Session() as session:
        response = session.get(f"{BASE_URL}/{seller_id}/item")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        response_data = response.json()
        assert isinstance(response_data, list), "Returned data is not a list"
        assert len(response_data) > 0, "Expected to return at least one item"
        print("items_data:", response_data)

def test_get_items_by_invalid_seller_id():
    invalid_seller_id = 11111223
    with requests.Session() as session:
        response = session.get(f"{BASE_URL}/{invalid_seller_id}/item")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        response_data = response.json()
        assert response_data == [], "Expected an empty list, but got data: {}".format(response_data)


