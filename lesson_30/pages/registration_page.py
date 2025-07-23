from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def fill_name(self, name):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupName"))).send_keys(name)

    def fill_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupLastName"))).send_keys(last_name)

    def fill_email(self, email):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupEmail"))).send_keys(email)

    def fill_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupPassword"))).send_keys(password)

    def fill_repeat_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "signupRepeatPassword"))).send_keys(password)

    def click_register(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))).click()

    def register_user(self, name, last_name, email, password):
        self.fill_name(name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_repeat_password(password)
        self.click_register()
