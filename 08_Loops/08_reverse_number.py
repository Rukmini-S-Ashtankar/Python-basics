number = int(input("Enter a number: "))
reverse = 0 

for _ in range(len(str(number))):
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse:", reverse)
