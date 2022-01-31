#!/usr/bin/python3
"""
4. Only sub class of
Write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
        Args:
            obj: object to check
            a_class: class to look into
    """
    if issubclass(type(obj), a_class):
        if type(obj) is a_class:
            return False
        return True
    return False
