from functools import reduce

marks = [75, 82, 64, 90, 55]

updated_marks = list(
    map(lambda mark: mark + 5, marks)
)

passed_marks = list(
    filter(lambda mark: mark >= 70, updated_marks)
)

total = reduce(
    lambda a, b: a + b,
    updated_marks
)

print("Updated marks:", updated_marks)
print("Marks 70 or above:", passed_marks)
print("Total marks:", total)
