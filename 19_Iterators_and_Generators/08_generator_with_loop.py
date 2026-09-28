def countdown(number):
    while number > 0:
        yield number
        number -= 1


for number in countdown(5):
    print(number)
