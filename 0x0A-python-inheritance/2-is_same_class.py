#!/usr/bin/python3
"""
2. Exact same object
Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
        Args:
            obj: object to check
            a_class: class to check if obj is into
    """
    if type(obj) is a_class:
        return True
    return False
