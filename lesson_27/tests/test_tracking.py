

def test_tracking_status(tracking_page, tracking_data):
    ttn, expected_status = tracking_data
    tracking_page.open()
    tracking_page.enter_tracking_number(ttn)
    status = tracking_page.get_current_status()
    assert status == expected_status, f"\nОчікували: '{expected_status}'\nОтримали: '{status}'"

