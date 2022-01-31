#!/usr/bin/python3
"""
10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle
"""importing rectangle as a parent class"""


class Square(Rectangle):
    """class Square is a sub class of Rectangle"""

    def __init__(self, size):
        """defining Square
            size: side of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of the square"""
        return self.__size * self.__size