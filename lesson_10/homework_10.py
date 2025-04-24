import unittest
from log_event_function import log_event

def read_last_log_line(log_path="login_system.log"):
    with open(log_path, "r") as f:
        lines = f.readlines()
        last_line = lines[-1] if lines else ""
        return lines, last_line


class TestHomework10(unittest.TestCase):

    def test_01_success_status(self):
        username = "Ales"
        status = "success"
        log_event(username, status)
        _, last_line = read_last_log_line()
        self.assertIn("INFO", last_line)
        self.assertIn(username, last_line)
        self.assertIn(status, last_line)

    def test_02_expired_status(self):
        username = "Ales"
        status = "expired"
        log_event(username, status)
        _, last_line = read_last_log_line()
        self.assertIn("WARNING", last_line)
        self.assertIn(username, last_line)
        self.assertIn(status, last_line)

    def test_03_failed_status(self):
        username = "Ales"
        status = "failed"
        log_event(username, status)
        _, last_line = read_last_log_line()
        self.assertIn("ERROR", last_line)
        self.assertIn(username, last_line)
        self.assertIn(status, last_line)

if __name__ == "__main__":
    unittest.main()
