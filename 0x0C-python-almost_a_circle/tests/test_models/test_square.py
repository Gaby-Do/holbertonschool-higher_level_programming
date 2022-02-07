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

    def test_x(self):
        self.assertRaises(ValueError, Square, 2, -5)
        for x in ['a', 'hola', (1, 2)]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, Square, 2, x)

    def test_y(self):
        self.assertRaises(ValueError, Square, 2, 5, -2)
        for y in ['a', 'hola', (1, 2)]:
            with self.subTest(y=y):
                self.assertRaises(TypeError, Square, 2, 2, y)
    
    def test_area(self):
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)




if __name__ == '__main__':
    unittest.main()
