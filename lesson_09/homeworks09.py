def sum_even_number(lst):
    """Функція, яка обчислює суму всіх парних чисел у списку."""
    return sum([item for item in lst if item % 2 == 0])

def sum_of_two_numbers(a, b):
    """  Функція, яка обчислює суму двох чисел."""
    return a + b

def filter_strings(lst):
    """Функція, яка приймає список і повертає новий список, що містить лише рядкові елементи"""
    return [item for item in lst if isinstance(item, str)]

    """  Функція, яка приймає список слів та повертає найдовше слово у списку."""
def find_longest_word(words):
    if words:
        return max(words, key=len)