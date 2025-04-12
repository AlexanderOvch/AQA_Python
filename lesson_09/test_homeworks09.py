import unittest
import logging
from homeworks09 import sum_even_number, sum_of_two_numbers, filter_strings, find_longest_word

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TestHomeworks(unittest.TestCase):

    # Тест для функції sum_even_number:
    def test_01(self):
        logging.info("Тест_01: sum_even_number")
        result = sum_even_number([1, 2, 3, 4])
        self.assertEqual(result, 6)  # Парні числа: 2 і 4, їх сума = 6
        logging.info("Успушно пройшов Тест_01: test_sum_even_number\n")

    def test_02(self):
        logging.info("Тест_02: sum_even_number_empty_list")
        result = sum_even_number([])
        self.assertEqual(result, 0)  # Порожній список, сума = 0
        logging.info("Успушно пройшов Тест_02: test_empty_list\n")

    # Тест для функції sum_of_two_numbers:
    def test_03(self):
        logging.info("Тест: sum_of_two_numbers_positive")
        result = sum_of_two_numbers(2, 3)
        self.assertEqual(result, 5)  # Очікувана сума: 2 + 3 = 5
        logging.info("Успушно пройшов Тест_03: test_sum_of_two_numbers\n")

    def test_04(self):
        logging.info("Тест_04: sum_of_two_numbers_negative_01")
        result = sum_of_two_numbers(-2, 3)
        self.assertEqual(result, 1)  # Очікувана сума: -2 + 3 = 1
        logging.info("Успушно пройшов Тест_04: test_sum_of_two_numbers\n")

    def test_05(self):
        logging.info("Тест_05: sum_of_two_numbers_negative_02")
        result = sum_of_two_numbers(-5, -3)
        logging.debug(f"Результат виконання: {result}")
        self.assertEqual(result, -8, f"Очікувалося -8, але отримано {result}")
        logging.info("Успушно пройшов Тест_05: test_sum_of_two_numbers_negative\n")

    # Тест для функції test_filter:
    def test_06(self):
        logging.info("Тест_06: filter_strings")
        result = filter_strings([1, 2, 3, "a", "b", "c","123"])
        self.assertEqual(result, ["a", "b", "c","123"])
        logging.info("Успушно пройшов Тест_06: test_filter_string\n")

    def test_07(self):
        logging.info("Тест_07: filter_strings_empty_list")
        result = filter_strings([])
        self.assertEqual(result, [])
        logging.info("Успушно пройшов Тест_07: test_filter_string_empty_list\n")

    def test_08(self):
        logging.info("Тест_08: test_filter_strings_empty_and_non_strings")

        # Тест для пустого списка
        result_empty = filter_strings([])
        logging.debug(f"Результат виконання для порожнього списку: {result_empty}")
        self.assertEqual(result_empty, [], f"Очікувалося [], але отримано {result_empty}")

        # Тест для списка без строк
        result_non_strings = filter_strings([1, 2.5, True, None])
        logging.debug(f"Результат виконання для списку без рядків: {result_non_strings}")
        self.assertEqual(result_non_strings, [], f"Очікувалося [], але отримано {result_non_strings}")

        logging.info("Успушно пройшов Тест_08: test_filter_strings_empty_and_non_strings\n")

    # Тест для функції find_longest_word:
    def test_09(self):
        logging.info("Тест_09: find_longest_word")
        result = find_longest_word(["трійка", "вчитель", "гвинтокрил", "мавпа"])
        assert result == "гвинтокрил", f"Очікувалося 'гвинтокрил', але отримано {result}"
        logging.info("Успушно пройшов Тест_09: find_longest_word\n")

    def test_10(self):
        logging.info("Тест_10: test_equal_length_words")
        result = find_longest_word(["кот", "рак", "ліс"])
        logging.debug(f"Результат виконання: {result}")
        assert result == "кот", f"Очікувалося 'кот', але отримано {result}"
        logging.info("Успушно пройшов Тест_10: test_equal_length_words\n")

if __name__ == "__main__":
    unittest.main()
