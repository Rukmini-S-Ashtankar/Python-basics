import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(
    url,
    params=params,
    timeout=10
)

response.raise_for_status()

posts = response.json()

print("Posts by User 1:")

for post in posts:
    print(post["title"])
