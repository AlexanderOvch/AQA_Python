import pytest
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(file_format)
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"

def validate_car_item(item):
    assert isinstance(item, dict)
    assert "brand" in item
    assert "year" in item
    assert "engine_volume" in item
    assert "price" in item


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 7),
    ("brand", 10),
    ("year", 0),
    ("price", 100),
    ("nonexistent", 5),  # негативний кейс
])
def test_search_cars(auth_session, sort_by, limit):
    logger.info(f"GET /cars?sort_by={sort_by}&limit={limit}")

    params = {"sort_by": sort_by, "limit": limit}
    response = auth_session.get(f"{BASE_URL}/cars", params=params)

    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    assert response.status_code in (200, 400)

    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, list)
        if limit > 0:
            assert len(data) <= limit
        for item in data:
            validate_car_item(item)
