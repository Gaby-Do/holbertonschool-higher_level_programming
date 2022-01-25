#!/usr/bin/python3
"""
2. Say my name
function that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """
    prints first_name and last_name,
    checks if they are strings,
    if not raises a TypeError with a msg
    """

    #check if arguments are strings
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
