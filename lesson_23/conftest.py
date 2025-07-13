import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"
    auth_data = HTTPBasicAuth('test_user', 'test_pass')

    response = session.post(auth_url, auth=auth_data)
    assert response.status_code == 200, "Authentication failed"

    token = response.json().get("access_token")
    assert token, "No token received"

    session.headers.update({"Authorization": f"Bearer {token}"})
    yield session
    session.close()
