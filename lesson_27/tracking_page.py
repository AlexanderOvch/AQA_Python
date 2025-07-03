from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.URL)

    def enter_tracking_number(self, number: str):
        input_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "en"))
        )
        input_field.clear()
        input_field.send_keys(number)

        search_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en"))
        )
        search_button.click()

    def get_current_status(self) -> str:
        try:
            # Пытаемся дождаться блока с реальным статусом
            status_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            )
            return status_element.text.strip()
        except TimeoutException:
            # Если не нашли статус, пробуем найти заголовок накладной
            try:
                bill_title = self.wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".tracking__bill-title"))
                )
                # Можно вернуть сам текст заголовка или написать "Накладна знайдена"
                return bill_title.text.strip()
            except TimeoutException:
                # Если и заголовка нет, ищем сообщение об ошибке
                try:
                    error_element = self.wait.until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//span[contains(text(),'Ми не знайшли посилку')]")
                        )
                    )
                    return error_element.text.strip()
                except TimeoutException:
                    # Если ничего не найдено — возвращаем дефолт
                    return "Статус не знайдено або помилка при отриманні даних"
