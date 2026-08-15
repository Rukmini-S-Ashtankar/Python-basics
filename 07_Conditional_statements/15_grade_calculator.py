marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
  grade = "A"
elif 75 <= marks < 90:
  grade = "B"
elif 60 <= marks < 75:
  grade = "C"
elif 40 <= marks < 60:
  grade = "D"
elif 0 <= marks < 40:
  grade = "F"
else:
  grade = "Invalid marks"

print("Grade:", grade)
