import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    print("API request successful!")
else:
    print("Request failed.")
    print("Status Code:", response.status_code)
