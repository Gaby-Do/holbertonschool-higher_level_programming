!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8)
- use the packages urllib and sys
- use the with statement
- email sent in the email variable
"""


import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    email = argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
