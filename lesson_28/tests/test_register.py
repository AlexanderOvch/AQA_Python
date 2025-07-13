import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_random_email():
    return "test_" + ''.join(random.choices(string.ascii_lowercase, k=8)) + "@mail.com"

def test_user_registration(driver, registration_page):
    email = generate_random_email()
    registration_page.register_user(
        name="Test",
        last_name="User",
        email=email,
        password="Qwerty123!"
    )

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Garage')]"))
        )
    except:
        try:
            error_element = driver.find_element(By.CLASS_NAME, "error-text")
            error_message = error_element.text
        except:
            error_message = "Error message not found"

        assert False, f"Registration failed. Message: {error_message}"
