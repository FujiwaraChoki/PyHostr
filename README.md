# PyHostr

Handle HTTP GET and POST requests in Python.

## Installation

```bash
pip install PyHostr
```

## Usage

```python
from PyHostr import PyHostr

# Instantiating the server
server = PyHostr("localhost", 8080)

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

[MIT Sami Hindi 2022 (c)](LICENSE.txt)
