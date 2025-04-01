# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("Task 01:")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= 25:
        result = number * multiplier

        print(f"{number}x{multiplier}={result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)

# task 2
print("\nTask 02:")
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a, b):
    return a + b

print(sum_of_two_numbers(3, 5))

# task 3
print("\nTask 03:")
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_of_list(numbers):
    if numbers:
        return sum(numbers) // len(numbers)
print(average_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# task 4
print("\nTask 04:")
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello, world!"))

# task 5
print("\nTask 05:")
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    if words:
        return max(words, key=len)

print(find_longest_word(["трійка", "вчитель", "гвинтокрил", "мавпа"]))

# task 6
print("\nTask 06:")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.lower().find(str2.lower())

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("\nTask 07:")
def filter_strings(lst):
    """Функція, яка приймає список і повертає новий список, що містить лише рядкові елементи"""
    return [item for item in lst if isinstance(item, str)]
print(filter_strings([1, 2, 3, "a", "b", "c","123"]))

# task 8
print("\nTask 07:")
def sum_even_number(lst):
    """Функція, яка обчислює суму всіх парних чисел у списку."""
    return sum([item for item in lst if item % 2 == 0])

print(sum_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# task 9
print("\nTask 09:")
def count(string):
    """Функція, яка перевіряє, чи містить рядок більше 10 унікальних символів"""
    return len(set(string)) > 10

print(count(input("Enter some text: ")))

# task 10
print("\nTask 10:")
def get_word_with_h():
    """Функція, яка запитує у користувача слово з літерою 'h' і повертає його."""
    while True:
        string = input("Enter word with 'h' letter: ")
        if "h" in string.lower():
            return string

print(get_word_with_h())

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""