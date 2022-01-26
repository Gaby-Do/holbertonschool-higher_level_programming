#!/usr/bin/python3
"""
    unitest for 6-max_integer.py
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """tests for max_integer function"""

    def test_list_integers(self):
        self.assertEqual(max_integer([45, 10, 252, 1]), 252)

    def test_list_floats(self):
        self.assertEqual(max_integer([45.0, 10.0, 252.0, 1.0]), 252.0)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        self.assertEqual(max_integer("1, 2, 3"), "3")
