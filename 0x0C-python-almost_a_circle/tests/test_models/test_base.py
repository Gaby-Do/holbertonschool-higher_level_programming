#!/usr/bin/python3
"""
    tests for 0x0C. Python - Almost a circle:
        task 1
"""


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """test Base id"""

    def test_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_int_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_no_id_2(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_str_id(self):
        b1 = Base('hola')
        self.assertEqual(b1.id, 'hola')

    def test_none_id(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 3)

    def test_neg_id(self):
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)


if __name__ == '__main__':
    unittest.main()
