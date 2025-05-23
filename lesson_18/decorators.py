from functools import wraps

def log_args_and_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функція: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції '{func.__name__}': {e}")
            return None
    return wrapper


if __name__ == "__main__":

    @log_args_and_result
    @handle_exceptions
    def divide(a, b):
        return a / b


    print(f"{divide(10, 2)}\n")

    print(f"{divide(10, 0)}\n")


