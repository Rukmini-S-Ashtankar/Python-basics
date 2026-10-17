import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Data fetched successfully!")
    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Unable to connect to the server.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
