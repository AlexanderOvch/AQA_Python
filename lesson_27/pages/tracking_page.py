from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from locators import TrackingLocators as Locators

class TrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    @property
    def tracking_input(self):
        return self.wait.until(EC.presence_of_element_located(Locators.TRACKING_INPUT.value))

    @property
    def search_button(self):
        return self.driver.find_element(*Locators.SEARCH_BUTTON.value)

    @property
    def status_text(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.STATUS_TEXT.value))

    @property
    def bill_title(self):
        return self.driver.find_element(*Locators.BILL_TITLE.value)

    def enter_tracking_number(self, ttn):
        self.tracking_input.clear()
        self.tracking_input.send_keys(ttn)
        self.search_button.click()

    def get_current_status(self):
        try:
            return self.status_text.text.strip()
        except TimeoutException:
            try:
                return self.bill_title.text.strip()
            except NoSuchElementException:
                try:
                    not_found = self.wait.until(
                        EC.visibility_of_element_located(Locators.NOT_FOUND_TEXT.value)
                    )
                    return not_found.text.strip()
                except Exception:
                    return "Статус не знайдено або помилка при отриманні даних"
