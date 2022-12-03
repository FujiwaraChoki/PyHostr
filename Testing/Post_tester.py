import requests

url = "http://localhost:8080/post"

r = requests.post(url, data={"TestKey": "TestValue"})

print(r.text)
