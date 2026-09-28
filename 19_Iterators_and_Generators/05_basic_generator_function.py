def numbers():
    yield 1
    yield 2
    yield 3


for number in numbers():
    print(number)
