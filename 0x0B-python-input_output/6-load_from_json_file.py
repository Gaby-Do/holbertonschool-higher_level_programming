#!/usr/bin/python3
"""
6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        return json.load(my_file)
