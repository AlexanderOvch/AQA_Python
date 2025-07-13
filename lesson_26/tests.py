import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:8000/dz.html"

frames_info = [
    {"id": "frame1", "input_id": "input1", "secret": "Frame1_Secret"},
    {"id": "frame2", "input_id": "input2", "secret": "Frame2_Secret"},
]

@pytest.mark.parametrize("frame", frames_info)
def test_frame_verification(driver, frame):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, frame["id"])))

    input_elem = wait.until(EC.presence_of_element_located((By.ID, frame["input_id"])))
    input_elem.clear()
    input_elem.send_keys(frame["secret"])

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    wait.until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()

    assert alert_text == "Верифікація пройшла успішно!", f"Помилка у {frame['id']} — отримано: {alert_text}"

    driver.switch_to.default_content()
