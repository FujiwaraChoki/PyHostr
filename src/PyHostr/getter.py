from pyhostr import PyHostr

def parse_data(args):

    print(args["text"])
    return str(args["text"]).upper()

def main():
    server: PyHostr = PyHostr("localhost", 8080)

    # Add a GET route
    server.get(route="/", response_headers={"Content-Type": "text/html"},
                response="<h2>INDEX PAGE</h2>")

    # Add a POST route
    server.post(route="/api", response_headers={"Content-Type": "application/json"},
                handler=parse_data)

    server.serve()


if __name__ == "__main__":
    main()

# How to make ngrok http 8080
# ngrok http 8080
