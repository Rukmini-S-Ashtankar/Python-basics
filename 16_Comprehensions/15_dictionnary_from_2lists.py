names = ["Rukmini", "Abhi", "Tanu"]
marks = [85, 92, 75]

student_marks = {
    name: mark
    for name, mark in zip(names, marks)
}

print(student_marks)
