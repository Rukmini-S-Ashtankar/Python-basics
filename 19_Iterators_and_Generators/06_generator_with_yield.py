def even_numbers(limit):
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number


for number in even_numbers(10):
    print(number)
