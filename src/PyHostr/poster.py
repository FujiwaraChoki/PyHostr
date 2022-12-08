import requests

url = "http://localhost:8080/api"
data = {
    "username": "admin",
    "password": "incorrect_password"
}

r = requests.post(url, data=data)

print(r.text)
