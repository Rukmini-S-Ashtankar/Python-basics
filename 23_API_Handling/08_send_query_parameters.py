import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2,
    "id": 11
}

response = requests.get(
    url,
    params=params,
    timeout=10
)
response.raise_for_status()

data = response.json()

for post in data:
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("-" * 30)
