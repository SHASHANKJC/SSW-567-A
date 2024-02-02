# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(a, b, c):  # renamed the function name to industry standard
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:    # error 1: adjusted the condition
        return 'Invalid Input'
        
    if a < 0 or b < 0 or c < 0:
        # error 1: replaced 0 instead of b and adjusted the condition and a side of the triangle cannot be 0
        return 'Invalid Input'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'Invalid Input'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):   # error 2: adjusted the condition
        return 'Invalid Input'
        
    # now we know that we have a valid triangle 
    if a == b and b == a and c == b:  # error 3: condition c==b is also essential to be equilateral
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2):
        # error 4: another * is missing in each () as well as each condition for right angle should be satisfied
        return 'Right'
    elif (a != b) and (b != c) and (a != c):   # error 5: c != a
        return 'Scalene'
    else:
        return 'Isosceles'
