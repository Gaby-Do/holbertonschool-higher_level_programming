#!/usr/bin/python3
"""
3. Print square
function that prints a square with the character #
"""


def print_square(size):
    """
        Arg:
            size (int): side of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            for i in range(size):
                print('#', end='')
            print()
