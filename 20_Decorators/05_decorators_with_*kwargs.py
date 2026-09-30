def decorator(function):
    def wrapper(**kwargs):
        print("Details:", kwargs)
        return function(**kwargs)

    return wrapper


@decorator
def student(name, age):
    print("Student:", name)
    print("Age:", age)


student(name="Riya", age=22)
