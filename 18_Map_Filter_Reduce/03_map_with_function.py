names = ["rukmini", "abhi", "ansh", "tanu"]

def make_uppercase(name):
    return name.upper()

result = list(map(make_uppercase, names))

print("Names:", result)
