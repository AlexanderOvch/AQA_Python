import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    @allure.step("Введення імені: {name}")
    def enter_name(self, name):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupName"))).send_keys(name)

    @allure.step("Введення прізвища: {last_name}")
    def enter_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupLastName"))).send_keys(last_name)

    @allure.step("Введення email: {email}")
    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupEmail"))).send_keys(email)

    @allure.step("Введення пароля")
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupPassword"))).send_keys(password)

    @allure.step("Повторне введення пароля")
    def enter_repeat_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupRepeatPassword"))).send_keys(password)

    @allure.step("Натискання кнопки 'Register'")
    def click_register(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))).click()

    @allure.step("Повна реєстрація користувача")
    def register_user(self, name, last_name, email, password):
        self.enter_name(name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_repeat_password(password)
        self.click_register()
