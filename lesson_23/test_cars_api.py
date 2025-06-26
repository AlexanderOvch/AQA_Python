import pytest
import requests
from requests.auth import HTTPBasicAuth
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

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"
    auth_data = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(auth_url, auth=auth_data)
    assert response.status_code == 200, "Authentication failed"

    token = response.json().get("access_token")
    assert token, "No token in response"
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:
    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 10),
        ("year", 0),
        ("price", 100),
        ("nonexistent", 5),
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        logger.info(f"Testing /cars?sort_by={sort_by}&limit={limit}")
        params = {
            "sort_by": sort_by,
            "limit": limit
        }
        response = auth_session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        assert response.status_code == 200 or response.status_code == 400

        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, list)
            if limit > 0:
                assert len(data) <= limit
            for item in data:
                assert "brand" in item
                assert "year" in item
                assert "engine_volume" in item
                assert "price" in item
