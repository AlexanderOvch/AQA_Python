import random
import string
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def generate_random_email():
    return "test_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@mail.com"

@allure.feature("Реєстрація")
@allure.story("Успішна реєстрація нового користувача")
@allure.title("Користувач може зареєструватися з валідними даними")
def test_user_registration(driver, registration_page):
    email = generate_random_email()

    try:
        with allure.step("Заповнення форми реєстрації"):
            registration_page.register_user(
                name="Test",
                last_name="User",
                email=email,
                password="Qwerty123!"
            )

        with allure.step("Очікування переходу на сторінку Garage"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Garage')]"))
            )
    except Exception as e:
        # При падении — скриншот ошибки
        allure.attach(driver.get_screenshot_as_png(), name="Скріншот при помилці", attachment_type=allure.attachment_type.PNG)
        raise e  # обязательно пробросить исключение дальше
    finally:
        # Всегда прикрепляем финальный скриншот — даже при падении
        allure.attach(driver.get_screenshot_as_png(), name="Фінальний стан", attachment_type=allure.attachment_type.PNG)
