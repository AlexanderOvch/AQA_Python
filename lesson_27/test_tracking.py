import pytest
from tracking_page import TrackingPage

def test_tracking_status(driver, tracking_data):
    ttn, expected_status = tracking_data
    page = TrackingPage(driver)
    page.open()
    page.enter_tracking_number(ttn)
    status = page.get_current_status()
    assert status == expected_status, f"Очікували: '{expected_status}', отримали: '{status}'"
