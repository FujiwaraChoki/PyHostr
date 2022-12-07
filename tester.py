import requests

def main():
    url = "http://localhost:8080/test-post"
    payload = {"name": "John"}
    
    r = requests.post(url, data=payload)
    print(r.text)

if __name__ == "__main__":
    main()
