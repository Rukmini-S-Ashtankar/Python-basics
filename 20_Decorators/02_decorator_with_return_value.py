def decorator(function):
    def wrapper():
        result = function()
        return result * 2

    return wrapper


@decorator
def number():
    return 10


print("Result:", number())
