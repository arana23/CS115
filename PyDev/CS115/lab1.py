'''
Created on Sep 6, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Aparajita Rana

CS115 - Lab 1
'''
from math import factorial
import math
import unittest
from cs115 import map, reduce


def __helprange(start, end, step=1):
    lst = []
    if step < 0:
        while start > end:
            lst += [start]
            start += step
    elif step > 0:
        while start < end:
            lst += [start]
            start += step
    else:
        raise ValueError('range() step argument cannot be zero.')
    return lst

def range(*args):
    '''range(stop) -> list of integers
       range(start,stop[,step]) -> list of integers
       Like list(range(...)) in Python 3.'''
    num_args = len(args)
    if num_args == 1: return __helprange(0, args[0])
    if num_args == 2: return __helprange(args[0], args[1])
    if num_args == 3: return __helprange(args[0], args[1], args[2])
    raise TypeError('range() must have 1, 2, or 3 arguments.')

def map(function, sequence):
    '''map(function, sequence) -> list
       Like list(map(...)) in Python 3.'''
    return [function(x) for x in sequence] if function != None \
        else [item for item in sequence if item]
        
def inverse(n):
    """Returns float value of 1/inputed number -> the inverse"""
    return (float(1.0/n))

def e(n):
    """creates 1st list made up of values 1 through n *inclusive* because of n+1"""
    mylist=range(1,n+1)
    """creates another list that calculates the factorial val of each item in mylist"""
    faclist=map(factorial,mylist)
    """creates last list that takes the inverse of the factorial val"""
    nextlist=map(inverse, faclist)
    """adds up all the values in nextlist and adds one"""
    return (sum(nextlist)+1)


def error(n):
    """returns the absolute value difference between the real e value and the e calculated above"""
    return abs(math.e-e(n))

class Test(unittest.TestCase):

    def testInverse1(self):
        self.assertAlmostEqual(inverse(1), 1, 6)

    def testInverse2(self):
        self.assertAlmostEqual(inverse(2), 0.5, 6)

    def testInverse3(self):
        self.assertAlmostEqual(inverse(3), 0.3333333333333333, 6)

    def testInverse4(self):
        self.assertAlmostEqual(inverse(-3), -0.3333333333333333, 6)

    def testE1(self):
        self.assertAlmostEqual(e(1), 2, 6)

    def testE2(self):
        self.assertAlmostEqual(e(2), 2.5, 6)

    def testE3(self):
        self.assertAlmostEqual(e(10), 2.718281801146385, 10)

    def testE4(self):
        self.assertAlmostEqual(e(100), 2.7182818284590455, 10)

    def testError1(self):
        self.assertAlmostEqual(error(1), 0.7182818284590451, 10)

    def testError2(self):
        self.assertAlmostEqual(error(2), 0.2182818284590451, 10)

    def testError3(self):
        self.assertAlmostEqual(error(10), 2.7312660133560485e-08, 10)

    def testError4(self):
        self.assertAlmostEqual(error(100), 4.440892098500626e-16, 10)

if __name__ == "__main__":
    unittest.main()