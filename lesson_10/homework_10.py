import unittest
from log_event_function import log_event


class TestHomework10(unittest.TestCase):

    def _run_test(self, username, status, expected_level, test_name):
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            last_line = lines[-1] if lines else ""

        # Просто убираем try/except, так как unittest сам поймает ошибки
        self.assertTrue(lines, "Лог-файл пуст")
        self.assertIn(expected_level, last_line, f"{test_name}: Ожидался уровень {expected_level}")
        self.assertIn(username, last_line, f"{test_name}: Username не найден в логе")
        self.assertIn(status, last_line, f"{test_name}: Status не найден в логе")

    # Тести

    def test_01_success_status(self):
        self._run_test(username="alex", status="success", expected_level="INFO", test_name="test_01_success_status")

    def test_02_expired_status(self):
        self._run_test(username="Nick", status="expired", expected_level="WARNING", test_name="test_02_expired_status")

    def test_03_invalid_status(self):
        self._run_test(username="Dima", status="failed", expected_level="ERROR", test_name="test_03_invalid_status")

    def test_04_empty_username(self):
        self._run_test(username="", status="success", expected_level="INFO", test_name="test_empty_username")

if __name__ == "__main__":
    unittest.main()
