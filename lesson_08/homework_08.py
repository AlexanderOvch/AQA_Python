def sum_numbers_in_string(s):
    try:
        numbers = s.split(',')
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"

data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
for item in data:
    result = sum_numbers_in_string(item)
    print(result)
