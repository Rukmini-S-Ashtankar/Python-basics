import re

phone = input("Enter a 10-digit mobile number: ")

pattern = r"[6-9]\d{9}"

if re.fullmatch(pattern, phone):
    print("Number format looks valid.")
else:
    print("Invalid number format.")
