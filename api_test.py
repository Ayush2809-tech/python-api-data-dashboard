import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    posts = response.json()

    print("API connected successfully!")
    print("Total posts:", len(posts))
    print("First post:", posts[0]['title'])
    for post in posts[:5]:
        print(f"Post ID: {post['id']}, Title: {post['title']}")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)