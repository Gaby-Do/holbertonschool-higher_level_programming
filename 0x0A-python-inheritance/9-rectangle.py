#!/usr/bin/python3
"""
6. Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import class BaseGeometry"""


class Rectangle(BaseGeometry):
    """class Rectangle is a sub class of BaseGeometry"""
    def __init__(self, width, height):
        """width and height must be integers"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """design an specific format output for printing"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
