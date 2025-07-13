# locators/tracking_locators.py
from selenium.webdriver.common.by import By

class TrackingLocators:
    TRACKING_INPUT = (By.ID, "en")
    SEARCH_BUTTON = (By.ID, "np-number-input-desktop-btn-search-en")
    STATUS_TEXT = (By.CSS_SELECTOR, ".header__status-text")
    BILL_TITLE = (By.CSS_SELECTOR, ".tracking__bill-title")
    NOT_FOUND_TEXT = (By.CSS_SELECTOR, "span[data-v-0b0e849a]")

