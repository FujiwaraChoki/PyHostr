# PyHost

Handle HTTP GET and POST requests in Python.

## Installation

```bash
pip install pyhost
```

## Usage

```python
from pyhost import PyHost

# Instantiating the server
server = PyHost("localhost", 8080)

# Creating a GET route
server.get(route="/", response_headers={"Content-type": "text/html"},
            response="<h2>INDEX PAGE</h2>")

# Creating a POST route
server.post(
    route="/post", response_headers={"Content-type": "application/json"}, handler=handler_func)

# Finally, start the server
server.serve()
```

## License

[MIT Sami Hindi 2022 (c)](https://choosealicense.com/licenses/mit/)
