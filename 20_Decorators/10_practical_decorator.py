def log_activity(function):
    def wrapper(username):
        print("Logging in...")
        result = function(username)
        print("Activity recorded.")

        return result

    return wrapper


@log_activity
def login(username):
    print(f"Welcome, {username}!")


login("Riya")
