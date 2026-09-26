numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
