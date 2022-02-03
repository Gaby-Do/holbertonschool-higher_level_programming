#!/usr/bin/python3
"""
1. Base class
Write the first class Base
"""


class Base():
    """
    This is my Base class

    Attributes:
        __nb_objects: (private class attr.) number of class objects
        id: (public instance attr.) (int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
