#!/usr/bin/python3
"""
13. Can I?
Write a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(mc, name, other):
    """ adds a new attribute to an object"""
    if not hasattr(mc, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(mc, name, other)
