from enum import Enum
from selenium.webdriver.common.by import By

class TrackingLocators(Enum):
    TRACKING_INPUT = (By.ID, "en")
    SEARCH_BUTTON = (By.ID, "np-number-input-desktop-btn-search-en")
    STATUS_TEXT = (By.CSS_SELECTOR, ".header__status-text")
    BILL_TITLE = (By.CSS_SELECTOR, ".tracking__bill-title")
    NOT_FOUND_TEXT = (By.XPATH, "//span[contains(text(),'Ми не знайшли посилку')]")
