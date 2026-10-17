import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, timeout=10)
response.raise_for_status()

posts = response.json()

for post in posts[:5]:
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("-" * 40)
