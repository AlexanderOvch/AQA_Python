class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            result = self.current
            self.current += 1
            if result % 2 == 0:
                return result
        raise StopIteration


if __name__ == "__main__":

    data = [10, 20, 30, 40]
    rev = ReverseList(data)

    print(f"Зворотній вивід спску {data}")
    for item in rev:
        print(item)

    N = 10
    even_iter = EvenIterator(N)
    print(f"\nПарні числа від 0 до {N}")
    for even_num in even_iter:
        print(even_num)
