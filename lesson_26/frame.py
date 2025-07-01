from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://localhost:8000/dz.html"

frame_data = {
    "frame1": ("input1", "Frame1_Secret"),
    "frame2": ("input2", "Frame2_Secret")
}

options = Options()
driver = webdriver.Chrome(options=options)

try:
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    for frame_id, (input_id, secret_value) in frame_data.items():
        print(f"\nПерехід у фрейм: {frame_id}")

        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, frame_id)))

        input_elem = wait.until(EC.presence_of_element_located((By.ID, input_id)))
        input_elem.clear()
        input_elem.send_keys(secret_value)

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert з фрейму {frame_id}: {alert_text}")

        assert alert_text == "Верифікація пройшла успішно!", f"Невірне повідомлення в {frame_id}!"

        alert.accept()

        driver.switch_to.default_content()
        print(f"{frame_id} перевірено успішно.")

    print("\nУсі фрейми перевірені успішно!")

finally:
    driver.quit()
