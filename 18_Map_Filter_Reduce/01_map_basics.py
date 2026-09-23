numbers = [1, 2, 3, 4, 5]

def square(number):
    return number ** 2

result = list(map(square, numbers))

print("Squares:", result)
