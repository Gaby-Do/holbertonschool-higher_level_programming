#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """
    this is class rectangle
    defined by width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Args:
            width: int >= 0, width of the rectangle
            Height: int >= 0, height of the rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        return self.height * self.width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return str('')

        new = ''
        for i in range(self.height):
            for j in range(self.width):
                new = new + str(self.print_symbol)
            if i < (self.height - 1):
                new = new + '\n'
        return new

    def __repr__(self):
        return (type(self).__name__ + "(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if rect_1.area() >= rect_2.area():
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
