'''
Created on Sep 6, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Aparajita Rana

CS115 - Lab 1
'''
from math import factorial
import math
import unittest
import cs115

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