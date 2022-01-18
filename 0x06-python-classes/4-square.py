#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """this is class Square"""
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        return self.__size * self.__size
