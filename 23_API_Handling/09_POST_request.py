import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Learning Python APIs",
    "body": "Practicing POST requests in Python.",
    "userId": 1
}

try:
    response = requests.post(
        url,
        json=new_post,
        timeout=10
    )
    response.raise_for_status()

    print("Post created successfully!")
    print("Response:", response.json())

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
