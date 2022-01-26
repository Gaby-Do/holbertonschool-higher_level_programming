#!/usr/bin/python3
"""
    unitest for 6-max_integer.py
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """tests for max_integer function"""

    def test_list_integers(self):
        self.assertEqual(max_integer([252, 10, 48, 1]), 252)

    def test_list_floats(self):
        self.assertEqual(max_integer([45.0, 10.0, 252.0, 1.0]), 252.0)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        self.assertEqual(max_integer("1, 2, 3"), "3")

    def test_only_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_only_one_item(self):
        self.assertEqual(max_integer([8]), 8)

    def test_one_negative(self):
        self.assertEqual(max_integer([8, -2, 10]), 10)

    def test_max_in_mid(self):
        self.assertEqual(max_integer([8, 15, 10]), 15)

    def test_max_at_end(self):
        self.assertEqual(max_integer([8, -2, 10, 252]), 252)


