def decorator(function):
    def wrapper(*args):
        print("Arguments:", args)
        return function(*args)

    return wrapper


@decorator
def add(a, b, c):
    return a + b + c


print("Result:", add(10, 20, 30))
