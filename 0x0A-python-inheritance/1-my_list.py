#!/usr/bin/python3
"""
1. My list
Write a class MyList that inherits from list
"""


class MyList(list):
    """this is class MyList"""
    pass

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
