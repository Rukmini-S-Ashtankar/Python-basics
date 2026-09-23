from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(a, b):
    return a + b

result = reduce(add, numbers)

print("Sum:", result)
