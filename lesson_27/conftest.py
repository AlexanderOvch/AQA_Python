import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(params=[
    ("00000000000000", "Експрес-накладна посилки № 00000000000000"),
    ("20450212345678", "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609"),
], ids=["valid_ttn", "invalid_ttn"])
def tracking_data(request):
    return request.param