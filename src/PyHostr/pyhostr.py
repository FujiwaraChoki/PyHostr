from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


routes = []


class PyHostr():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    class Handler(BaseHTTPRequestHandler):

        def do_GET(self):
            print("Current path: " + self.path)
            # Handle GET requests, using objects in routes
            for obj in routes:
                if self.path == obj["route"] and str(obj["method"]).lower() == "get":
                    self.send_response(200)
                    # Send headers
                    for key, value in obj["response_headers"].items():
                        self.send_header(key, value)
                    self.end_headers()
                    self.wfile.write(
                        bytes(obj["response"], "utf8"))
                    return

            self.send_response(404)

        def do_POST(self):
            for obj in routes:
                if self.path == obj["route"] and str(obj["method"]).lower() == "post":
                    self.send_response(200)
                    # Send headers
                    self.end_headers()
                    # Send custom reply and parse into JSON
                    data = self.rfile.read(
                        int(self.headers['Content-Length']))\
                        .decode("utf-8")\
                        .split("&")
                    result = {}
                    for arg in data:
                        key, value = arg.split("=")
                        result[key] = value
        
                    self.wfile.write(bytes(obj["handler"](result), "utf8"))

                    return

    def warn(self, message):
        print(bcolors.WARNING + "WARNING:\t" + message + bcolors.ENDC)

    def error(self, message):
        print(bcolors.FAIL + "ERROR:\t" + message + bcolors.ENDC)

    def success(self, message):
        print(bcolors.OKGREEN + "SUCCESS:\t" + message + bcolors.ENDC)

    def msg(self, message):
        print("MSG:\t" + message)

    def get(self, route, response="<h1>Default Response</h1>", response_headers={"Content-type": "text/html"}):
        # Add route to routes
        routes.append({
            "method": "GET",
            "route": route,
            # The HTML response
            "response": response,
            "response_headers": response_headers
        })

    def post(self, route, response_headers, handler):
        # Handle POST requests, using objects in routes
        routes.append({
            "method": "POST",
            "route": route,
            "response": response_headers,
            # Handler is a function that handles the POST request
            "handler": handler
        })

    def serve(self):
        # Start server
        server = HTTPServer((self.host, self.port), PyHostr.Handler)
        self.success("Server started http://%s:%s" %
                     (self.host, self.port))

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            self.warn("\nStopping server...")
            self.success("Server stopped")
        server.server_close()
        print("Server stopped.")


# Showcase of PyHostr Usage

# This is a handler function which you specify when calling the post() method.
# NOTE: MAKE SURE TO NOT USE PARANTHESES WHEN PASSING THE FUNCTION TO THE post() METHOD

def parse_data(args):
    result = {}
    for arg in args:
        key, value = arg.split("=")
        result[key] = value
    return json.dumps(result)


def handler_func(args):
    return str(args["name"]).upper()


if __name__ == "__main__":
    # Create a PyHostr object
    server = PyHostr("localhost", 8080)

    # Add a GET route
    server.get(route="/", response_headers={"Content-Type": "text/html"},
               response="<h2>INDEX PAGE</h2>")

    # Add a POST route
    server.post(
        route="/test-post", response_headers={"Content-type": "application/json"}, handler=handler_func)  # Don't use parentheses when passing the function

    # Start server on port 8080
    server.serve()
