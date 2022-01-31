#!/usr/bin/python3
"""
12. My integer
Write a class MyInt that inherits from int
"""


class MyInt(int):
    """MyInt has == and != operators inverted"""
    def __eq__(self, operador):
        """changes == to !="""
        return False

    def __ne__(self, operator):
        """changes != to =="""
        return True
