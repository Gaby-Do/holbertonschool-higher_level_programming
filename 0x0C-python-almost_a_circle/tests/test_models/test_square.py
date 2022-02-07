#!/usr/bin/python3
"""Tests for Square"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """testing Square"""

    def test_empty(self):
        self.assertRaises(TypeError, Square, ())

    def test_size(self):
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(TypeError, Square, (1, 2))
        self.assertRaises(TypeError, Square, 'a')
