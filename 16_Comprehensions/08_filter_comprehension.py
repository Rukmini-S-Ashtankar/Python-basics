marks = {
    "Rukmini": 85,
    "Riya": 45,
    "Tanu": 72,
    "Mina": 38
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >= 50
}

print("Passed students:", passed)
