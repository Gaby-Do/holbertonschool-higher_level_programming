#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """
    this is class rectangle
    defined by width and height
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width: int >= 0, width of the rectangle
            Height: int >= 0, height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width
            Arg:
                value: must be int >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height
            Arg:
                value: must be int >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return str('')

        new = ''
        for i in range(self.__height):
            for j in range(self.__width):
                new = new + '#'
            if i < (self.__height - 1):
                new = new + '\n'
        return new

    def __repr__(self):
        return (type(self).__name__ + "(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
