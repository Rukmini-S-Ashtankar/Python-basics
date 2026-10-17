import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)
response.raise_for_status()

user = response.json()

print("Name:", user["name"])
print("Username:", user["username"])
print("Email:", user["email"])
print("City:", user["address"]["city"])
