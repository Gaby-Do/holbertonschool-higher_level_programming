#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
- use the packages requests and sys
"""

import requests
from sys import argv


if __name__ == "__main__":
	x = requests.get(argv[1])
	print(x.headers.get('X-Request-Id'))
