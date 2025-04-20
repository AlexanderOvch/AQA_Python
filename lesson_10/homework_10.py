import unittest
import logging
from log_event_function import log_event

# налаштуваяння для логування login функції
logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)
open("login_system.log", "w").close() # Чистка файлу login_system.log при старті тестів

if not logger.handlers:
    fh = logging.FileHandler("login_system.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# налаштуваяння для логування юніттестів в окремий файл
test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.INFO)
open("test_log.log", "w").close()  # Чистка файлу test_log.log при старті тестів

if not test_logger.handlers:
    test_fh = logging.FileHandler("test_log.log")
    test_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    test_fh.setFormatter(test_formatter)
    test_logger.addHandler(test_fh)


class TestHomework10(unittest.TestCase):

    def _run_test(self, username, status, expected_level, test_name): #стартовий ран в який ми будемо вписувати данні
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            last_line = lines[-1] if lines else ""

        try:
            self.assertTrue(lines, "Лог-файл пуст")
            self.assertIn(expected_level, last_line, f"{test_name}: Ожидался уровень {expected_level}")
            self.assertIn(username, last_line, f"{test_name}: Username не найден в логе")
            self.assertIn(status, last_line, f"{test_name}: Status не найден в логе")

            # Тест пассед
            test_logger.info(f"{test_name} PASSED: {last_line.strip()}")

        except AssertionError as e:
            # Логування якщо фейл
            test_logger.error(f"{test_name} FAILED: {e}")
            raise

    # Тести

    def test_01_success_status(self):
        self._run_test(username="alex", status="success", expected_level="INFO", test_name="test_01_success_status")

    def test_02_expired_status(self):
        self._run_test(username="Nick", status="expired", expected_level="WARNING", test_name="test_02_expired_status")

    def test_03_invalid_status(self):
        self._run_test(username="Dima", status="failed", expected_level="ERROR", test_name="test_03_invalid_status")

    def test_04_empty_username(self):
        self._run_test(username="", status="success", expected_level="success", test_name="test_empty_username")

if __name__ == "__main__":
    unittest.main()
