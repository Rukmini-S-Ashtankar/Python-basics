marks = {
    "Rukmini": 90,
    "Abhi": 92,
    "Tanu": 83
}

highest = max(marks, key=lambda name: marks[name])

print("Highest scorer:", highest)
