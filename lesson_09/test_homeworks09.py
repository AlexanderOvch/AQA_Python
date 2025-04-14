import unittest
import logging
from homeworks09 import sum_even_number, sum_of_two_numbers, filter_strings, find_longest_word

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TestHomeworks(unittest.TestCase):

    # Тест для функції sum_even_number:
    def test_01_Sum_even_number(self):
        logging.info("Тест_01: sum_even_number")
        result = sum_even_number([1, 2, 3, 4])
        self.assertEqual(result, 6)  # Парні числа: 2 і 4, їх сума = 6
        logging.info("Успушно пройшов Тест_01: test_sum_even_number\n")

    def test_02_sum_even_number_empty_list(self):
        logging.info("Тест_02: sum_even_number_empty_list")
        result = sum_even_number([])
        self.assertEqual(result, 0)  # Порожній список, сума = 0
        logging.info("Успушно пройшов Тест_02: test_empty_list\n")

    def test_03_invalid_input_type(self):
        logging.info("Тест_03: sum_even_number_invalid_type")
        with self.assertRaises(TypeError):
            sum_even_number("abc")  # Пытаемся передать строку вместо списка
        logging.info("Успішно пройшов Тест_03: sum_even_number_invalid_type\n")

    # Тест для функції sum_of_two_numbers:
    def test_04_sum_of_two_numbers_positive(self):
        logging.info("Тест_04: sum_of_two_numbers_positive")
        result = sum_of_two_numbers(2, 3)
        self.assertEqual(result, 5)  # Очікувана сума: 2 + 3 = 5
        logging.info("Успушно пройшов Тест_04: test_sum_of_two_numbers\n")

    def test_05_sum_of_negative_and_postive_number(self):
        logging.info("Тест_05: sum_of_negative_and_postive_number")
        result = sum_of_two_numbers(-2, 3)
        self.assertEqual(result, 1)  # Очікувана сума: -2 + 3 = 1
        logging.info("Успушно пройшов Тест_05: sum_of_negative_and_postive_number\n")

    def test_06_sum_of_two_negative_number(self):
        logging.info("Тест_06: sum_of_two_negative_number")
        result = sum_of_two_numbers(-5, -3)
        logging.debug(f"Результат виконання: {result}")
        self.assertEqual(result, -8, f"Очікувалося -8, але отримано {result}")
        logging.info("Успушно пройшов Тест_06: sum_of_two_negative_number\n")

    def test_07_invalid_input_type_sum_of_two_numbers(self):
        logging.info("Тест_07: sum_of_two_numbers_invalid_type")
        with self.assertRaises(TypeError):
            sum_of_two_numbers("2", 3)  # Пытаемся передать строку вместо числа
        logging.info("Успушно пройшов Тест_07: sum_of_two_numbers_invalid_type\n")

    # Тест для функції test_filter:
    def test_08_filter_strings(self):
        logging.info("Тест_08: filter_strings")
        result = filter_strings([1, 2, 3, "a", "b", "c","123"])
        self.assertEqual(result, ["a", "b", "c","123"])
        logging.info("Успушно пройшов Тест_08: test_filter_string\n")

    # Тест для пустого списка
    def test_09_filter_strings_empty_list(self):
        logging.info("Тест_09: filter_strings_empty_list")
        result_empty = filter_strings([])
        logging.debug(f"Результат виконання для порожнього списку: {result_empty}")
        self.assertEqual(result_empty, [], f"Очікувалося [], але отримано {result_empty}")
        logging.info("Успушно пройшов Тест_09: filter_strings_empty_list\n")

    # Тест для списка без строк
    def test_10_filter_non_strings(self):
        logging.info("Тест_10: test_filter_non_strings")
        result_non_strings = filter_strings([1, 2.5, True, None])
        logging.debug(f"Результат виконання для списку без рядків: {result_non_strings}")
        self.assertEqual(result_non_strings, [], f"Очікувалося [], але отримано {result_non_strings}")
        logging.info("Успушно пройшов Тест_10: test_filter_non_strings\n")

    # Тест для функції find_longest_word:
    def test_11_find_longest_word(self):
        logging.info("Тест_11: find_longest_word")
        result = find_longest_word(["трійка", "вчитель", "гвинтокрил", "мавпа"])
        assert result == "гвинтокрил", f"Очікувалося 'гвинтокрил', але отримано {result}"
        logging.info("Успушно пройшов Тест_11: find_longest_word\n")

    def test_12_test_equal_length_words(self):
        logging.info("Тест_12: test_equal_length_words")
        result = find_longest_word(["кот", "рак", "ліс"])
        logging.debug(f"Результат виконання: {result}")
        assert result == "кот", f"Очікувалося 'кот', але отримано {result}"
        logging.info("Успушно пройшов Тест_12: test_equal_length_words\n")

    def test_13_invalid_input_type_equal_length_words(self):
        logging.info("Тест_13: find_longest_word_invalid_type")

        # Перевірка на рядок замість списку
        with self.assertRaises(TypeError):
            find_longest_word("кот, рак, ліс")

        # Перевірка на список з числами
        with self.assertRaises(TypeError):
            find_longest_word([1, 2, 3])

        # Перевірка на список з елементами, які не є рядками
        with self.assertRaises(TypeError):
            find_longest_word(["кот", 5, "ліс"])
        logging.info("Успішно пройшов Тест_13: find_longest_word_invalid_type\n")

if __name__ == "__main__":
    unittest.main()
