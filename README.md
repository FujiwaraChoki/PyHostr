# PyHost

Handle HTTP GET and POST requests in Python.

## Installation

```bash
pip install pyhost
```

## Usage

```python
from pyhost import PyHost

host = PyHost()

def on_get(request, response):
    response.send("Hello World!")§
```

## License

[MIT Sami Hindi 2022 (c)](https://choosealicense.com/licenses/mit/)
