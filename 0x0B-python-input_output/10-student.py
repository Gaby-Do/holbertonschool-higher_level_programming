#!/usr/bin/python3
"""
10. Student to JSON with filter
Idem 9. plus:
If attrs is a list of strings, only attribute names contained
in this list must be retrieved.
"""


class Student:
    """
    Student is defined by:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        if type(attrs) is not list:
            return
        if not attrs:
            return self.__dict__
        aux = {}
        for key in self.__dict__:
            if key in attrs:
                aux[key] = self.__dict__[key]
        return aux
