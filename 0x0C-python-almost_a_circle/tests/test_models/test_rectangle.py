#!/usr/bin/python3
"""Tests for Rectangle"""


import unittest

from models.base import Base

from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """testing Rectangle"""


    def test_empty(self):
        self.assertRaises(TypeError, Rectangle.__init__, ())

#Tests for width:

    def test_width(self):
        for w in [-1, 'a', 'hola', (1, 2), 0]:
            with self.subTest(w=w):
                self.assertRaises(TypeError, Rectangle.__init__, (w, 10, 1, 2, 3))
    
    def test_str_w(self):
        self.assertRaises(TypeError, Rectangle.__init__, ('a', 10))
    
    def test_neg_w(self):
        self.assertRaises(TypeError, Rectangle.__init__, (-1, 10))

#Tests for height:

    def test_height(self):
        for h in [-1, 'a', 'hola', (1, 2), 0]:
            with self.subTest(h=h):
                self.assertRaises(TypeError, Rectangle.__init__, (2, h))
    
#Tests for x:
    
    def test_x(self):
        for x in [-1, 'a', 'hola', (1, 2)]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, Rectangle.__init__, (2, 10, x))

#Tests for y:
    
    def test_y(self):
        for y in [-1, 'a', 'hola', (1, 2)]:
            with self.subTest(y=y):
                self.assertRaises(TypeError, Rectangle.__init__, (2, 10, 0, y))

#Tests for area:

    def test_area(self):
#        for h in [-1, 'a', 'hola', 0]:
#            with self.subTest(h=h):
        r1 = Rectangle(1, 2)
        self.assertEqual(Rectangle.area(r1), 2)
