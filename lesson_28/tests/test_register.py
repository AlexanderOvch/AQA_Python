import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def generate_random_email():
    return "test_" + ''.join(random.choices(string.ascii_lowercase, k=8)) + "@mail.com"

def test_user_registration(driver, registration_page):
    registration_page.name_input.send_keys("Test")
    registration_page.last_name_input.send_keys("User")
    email = generate_random_email()
    registration_page.email_input.send_keys(email)
    registration_page.password_input.send_keys("Qwerty123!")
    registration_page.repeat_password_input.send_keys("Qwerty123!")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
    )
    registration_page.register_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Garage')]"))
        )
    except:
        try:
            error_element = driver.find_element(By.CLASS_NAME, "error-text")
            error_message = error_element.text
            print(f"Registration error: {error_message}")
        except:
            error_message = None
            print("No error message")

        assert False, f"Registration failed. Message: {error_message}"
