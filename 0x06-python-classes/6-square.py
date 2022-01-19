#!/usr/bin/python3
"""5. Printing a square"""


class Square:
    """this is class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
            Args:
                size: size of the square
                position: tuple, square's position
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve size of the square"""
        return self.__size

    @property
    def position(self):
        return self.__position

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

    @position.setter
    def position(self, value):
        """sets position's value"""
        if (type(value) is not tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates and returns area"""
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(' ', end='')
                for i in range(self.__size):
                    print('#', end='')
                print()
