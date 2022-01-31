#!/usr/bin/python3
"""
3. Same class or inherit from
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
        Args:
            obj: object to check
            a_class: class to look if obj is into
    """
    if isinstance(obj, a_class):
        return True
    return False
