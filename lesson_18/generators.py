def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


if __name__ == "__main__":

    N = 10
    print(f"\nГенератор який повертає послідовність парних чисел від 0 до {N}")
    for numbers in even_numbers_generator(N):
        print(numbers)

    N = 50
    print(f"\nГенератор Фібоначчі з числом {N}")
    for number in fibonacci_generator(N):
        print(number)