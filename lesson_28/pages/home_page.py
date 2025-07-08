from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    @property
    def sign_up_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
