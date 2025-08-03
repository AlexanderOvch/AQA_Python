import random
import string
import allure

def generate_random_email():
    return "test_" + ''.join(random.choices(string.ascii_lowercase, k=8)) + "@mail.com"

@allure.feature("Реєстрація")
@allure.story("Успішна реєстрація нового користувача")
@allure.title("Користувач може зареєструватися з валідними даними")
def test_user_registration(driver, registration_page):
    email = generate_random_email()

    registration_page.register_user(
        name="Test",
        last_name="User",
        email=email,
        password="Qwerty123!"
    )

    assert registration_page.is_registration_successful(), "Реєстрація неуспішна або не перейшло на сторінку Garage"
