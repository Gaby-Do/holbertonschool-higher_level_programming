#!/usr/bin/python3
"""
0. Lookup
Write a function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    listing arguments and methos of an object
    Args:
        obj: object to lookup
    """
    return dir(obj)
