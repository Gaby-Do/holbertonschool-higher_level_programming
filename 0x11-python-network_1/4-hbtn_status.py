#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
- use the package requests
"""


import requests

x = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(x.text)))
print("\t- content: {}".format(x.text))
