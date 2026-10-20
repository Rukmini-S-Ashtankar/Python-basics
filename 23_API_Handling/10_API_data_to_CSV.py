import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    posts = response.json()

    with open(
        "api_posts.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "userId", "title", "body"]
        )

        writer.writeheader()
        writer.writerows(posts)

    print("API data saved to api_posts.csv")
    print("Total records:", len(posts))

except (requests.exceptions.RequestException, OSError) as error:
    print("Error:", error)
