def decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello!")


greet()
