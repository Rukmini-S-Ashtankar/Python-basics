numbers = [10, 15, 20, 25, 30]

def is_even(number):
    return number % 2 == 0

result = list(filter(is_even, numbers))

print("Even numbers:", result)
