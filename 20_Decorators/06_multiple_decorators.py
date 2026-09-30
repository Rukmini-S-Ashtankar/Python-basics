def uppercase(function):
    def wrapper():
        return function().upper()

    return wrapper


def add_message(function):
    def wrapper():
        return "Message: " + function()

    return wrapper


@add_message
@uppercase
def greet():
    return "hello python"


print(greet())
