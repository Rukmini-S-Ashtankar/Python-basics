def counter():
    number = 1

    while True:
        yield number
        number += 1


numbers = counter()

for _ in range(5):
    print(next(numbers))
