#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        set_q = {"q": argv[1]}
    else:
        set_q = {"q": ""}
    x = requests.post("http://0.0.0.0:5000/search_user", data=set_q)
    try:
        req = x.json()
        if len(req) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except Exception:
        print("Not a valid JSON")
