#!/usr/bin/python3
"""
1. My list
Write a class MyList that inherits from list
"""


class MyList(list):
    pass

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        aux_list = self[:]
        aux_list.sort()
        print(aux_list)
