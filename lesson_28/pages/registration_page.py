from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def name_input(self):
        return self.driver.find_element(By.ID, "signupName")

    @property
    def last_name_input(self):
        return self.driver.find_element(By.ID, "signupLastName")

    @property
    def email_input(self):
        return self.driver.find_element(By.ID, "signupEmail")

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, "signupPassword")

    @property
    def repeat_password_input(self):
        return self.driver.find_element(By.ID, "signupRepeatPassword")

    @property
    def register_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Register']")
