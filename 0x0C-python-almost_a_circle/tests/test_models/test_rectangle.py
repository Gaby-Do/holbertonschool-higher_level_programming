#!/usr/bin/python3
"""Tests for Rectangle"""


import unittest

from models.base import Base

from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """testing Rectangle"""


    def test_empty(self):
        self.assertRaises(TypeError, Rectangle, ())

#Tests for width:

    def test_width(self):
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, -1, 10)
        self.assertRaises(TypeError, Rectangle, (1, 2), 10)
        self.assertRaises(TypeError, Rectangle, 'a', 10)

#Tests for height:

    def test_height(self):
        for h in [-1, 0]:
            with self.subTest(h=h):
                self.assertRaises(ValueError, Rectangle, 2, h)
        for h in ['a', 'hola', (1, 2)]:
            with self.subTest(h=h):
                self.assertRaises(TypeError, Rectangle, 2, h)
    
#Tests for x:
    
    def test_x(self):
        self.assertRaises(ValueError, Rectangle, 2, 10, -5)
        for x in ['a', 'hola', (1, 2)]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, Rectangle, 2, 10, x)

#Tests for y:
    
    def test_y(self):
        self.assertRaises(ValueError, Rectangle, 2, 10, 2, -2)
        for y in ['a', 'hola', (1, 2)]:
            with self.subTest(y=y):
                self.assertRaises(TypeError, Rectangle, (2, 10, 0, y))

#Tests for area:

    def test_area(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(Rectangle.area(r1), 2)

