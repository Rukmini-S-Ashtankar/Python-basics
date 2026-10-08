import re

email = input("Enter your email: ")

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Email format looks valid.")
else:
    print("Invalid email format.")
