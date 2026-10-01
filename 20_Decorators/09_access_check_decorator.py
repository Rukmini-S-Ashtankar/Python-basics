def check_access(function):
    def wrapper(role):
        if role == "admin":
            return function(role)
        else:
            print("Access denied.")

    return wrapper


@check_access
def dashboard(role):
    print("Welcome to the dashboard!")


dashboard("admin")
dashboard("user")
