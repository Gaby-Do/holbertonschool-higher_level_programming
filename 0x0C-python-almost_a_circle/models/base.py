#!usr/bin/python3
"""
1. Base class
Write the first class Base
"""


import json
from os import path


class Base():
    """
    This is my Base class

    Attributes:
        __nb_objects: (private class attr.) number of class objects
        id: (public instance attr.) (int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_aux = []
            return list_aux
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open('{}.json'.format(cls.__name__), 'w+') as my_file:
            list_aux = []
            if list_objs is None:
                my_file.write(list_aux)
            else:
                for item in list_objs:
                    list_aux.append(cls.to_dictionary(item))
                my_file.write(cls.to_json_string(list_aux))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        list_aux = []
        if json_string is None:
            return list_aux
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            my_dummy = cls(2, 2)
        elif cls.__name__ == 'Square':
            my_dummy = cls(2)
        my_dummy.update(**dictionary)
        return my_dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_of_instances = []
        if path.isfile('{}.json'.format(cls.__name__)):
            with open('{}.json'.format(cls.__name__), 'r') as my_file:
                for row in my_file:
                    instance = cls.from_json_string(row)
                    for item in instance:
                        list_of_instances.append(cls.create(**item))
        return list_of_instances
