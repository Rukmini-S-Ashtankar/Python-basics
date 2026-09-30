def decorator(function):
    def wrapper(a, b):
        print("Calculating...")
        return function(a, b)

    return wrapper


@decorator
def add(a, b):
    return a + b


print("Result:", add(10, 20))
