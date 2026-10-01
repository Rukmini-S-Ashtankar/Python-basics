def repeat(times):
    def decorator(function):
        def wrapper():
            for _ in range(times):
                function()

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()
