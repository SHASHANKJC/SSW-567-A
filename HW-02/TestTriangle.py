# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(4, 3, 3), "Isosceles")
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(5, 4, 8), "Scalene")
        self.assertEqual(classify_triangle(10, 5, 8), "Scalene")
        self.assertEqual(classify_triangle(6, 9, 8), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(16, 63, 65), "Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Right")
        self.assertEqual(classify_triangle(8, 15, 17), "Right")

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid Input")
        self.assertEqual(classify_triangle(3, 1.143, 5), "Invalid Input")
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid Input")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
