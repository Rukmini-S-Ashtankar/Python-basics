def expense_generator(expenses):
    for expense in expenses:
        yield expense


expenses = [500, 1200, 300, 750]

for amount in expense_generator(expenses):
    print("Expense: ₹", amount)
