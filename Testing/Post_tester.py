import requests

url = "http://localhost:8080/post"

r = requests.post(url)

print(r.text)
