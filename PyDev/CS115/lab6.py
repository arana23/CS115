'''
Created on 10/10/2018
@author:   arana3 - Aparajita Rana
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - Aparajita Rana

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if(n%2==0):
        return False
    return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif(isOdd(n)== True):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif int (s[-1]) == 1:
        return 1+2*(binaryToNum(s[:-1]))
    else:
        return 2*binaryToNum(s[:-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    a=binaryToNum(s)+1
    b=numToBinary(a)
    if 8<len(b):
        return b[-8:]
    return ('0'*(8-len(b)))+b

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==0:
        print(s)
    else:
        print(s)
        s=increment(s)
        count(s,n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n%3 == 1:
        return numToTernary(int(n/3))+'1'
    elif n%3 == 2:
        return numToTernary(int(n/3))+'2'
    return numToTernary(n/3)+'0'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if len(s) == 1:
        return int(s)
    return 3*ternaryToNum(s[:-1])+int(s[-1])
