#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """this is class Square"""
    def __init__(self, size=0):
        """
            Arg:
                size: size of the square
        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """retrieve size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size
            Arg:
                value: value for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        return self.__size * self.__size
