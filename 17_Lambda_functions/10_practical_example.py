products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500}
]

products.sort(key=lambda product: product["price"])

for product in products:
    print(product["name"], "-", product["price"])
