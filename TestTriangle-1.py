# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import pytest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(pytest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTriangles2(self):
            self.assertNotEqual(classifyTriangle(15, 15, 15),'Equilateral','15,15,15 should be Equilateral')
    
    def testEquilateralTriangle3(self):
        self.assertNotEqual(classifyTriangle(10, 1, 10), 'Equilateral','10,1,10 should be Equilateral')

    # Testing Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles','5,5,3 should be Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isosceles','4.6.6 is a Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(8, 5, 8), 'Isosceles','8,5,8 is a Isosceles')

    def testIsoscelesTriangle4(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isosceles','6,6,4 is a isosceles')

    # Testing Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene','10,11,12 should be isosceles')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene','4,2,3 is a Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(100, 110, 112), 'Scalene','100,110,112 is a Scalene')

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(10, 10, 12), 'Scalene','10,10,12 is a Scalene')

    # Testing Invalid Inputs
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle("200", "0", "0"), 'InvalidInput')

    # Testing Not a Triangle
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(1, 5, 1), 'NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(1, 1, 5), 'NotATriangle')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(1, 17, 5), 'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    pytest.main()


