numbers = []

for i in range(5):
  num = int(input("Enter a number: "))
  numbers.append(num)

print("\n Original List: ", numbers)

print("Length: ", len(numbers))
print("Maximum: ", max(numbers))
print("Minimum: ", min(numbers))
print("Sum: ", sum(numbers))
print("Average: ", sum(numbers) / len(numbers))

numbers.sort()
print("Sorted List: ", nnumbers)

numbers.reverse()
print("Reversed List: ", numbers)
