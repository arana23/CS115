'''
Created on Oct 29, 2018

@author: arana3 - Aparajita Rana

Pledge: I pledge my honor that I have abided by the Stevens Honor System - Aparajita Rana

CS115 - Hw 8
'''
from CS115.hw6 import numToBinary

COMPRESSED_BLOCK_SIZE = 5

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

#slighty modified numtobinary in order to have w/o isOdd
def numToBinary(n):
    '''Takes in an integer, n, and returns  its binary representation.'''
    if n == 0:
        return ''
    return numToBinary(int(n/2)) + str(n % 2)

def zeroify(x):
    # 5 zeros before binary number
    return (COMPRESSED_BLOCK_SIZE-len(x))*"0"+x

def numtchelper(s):
    #flips the values if empty return nothing, a 0 changes to a 1, and 
    if s=='':
        return ''
    #if zero flip to one
    elif s[0]=='0':
        return '1'+numtchelper(s[1:])
    #must be 1 so flip to 0
    else:
        return '0'+numtchelper(s[1:])

def increment(s):
    #Returns the binary rep of binaryToNum(s) + 1
    if s=='':
        return ''
    res=binaryToNum(s)+1
    return numToBinary(res)

def TcToNum(s):
    #takes string of 8 bits in two's-complement, and returns the corresponding integer
    if s == '':
        return 0
    # if 0 -> normal positive return binarytoNum
    if s[0] == '0':
        return binaryToNum(s)
    # if 1 increment and flip
    if s[0] == '1':
        res = increment(numtchelper(s))
        return (binaryToNum(res))*-1
    
def NumToTc(n):
    #takes val in -128 to 127 (max vals for 8 bit) -> returns the two's-compliment representation
    if n=='' or n==0:
        return "00000000"
    #check range n is in, accordingly multiply by -1 & use 8-len(res)
    elif -129 < n < 0:
        res=numToBinary(n*-1)
        if len(res)<8:
            return increment(numtchelper((8-len(res))*'0'+res))
        else:
            return increment(numtchelper(res))
    # if n is positive number res is simply numtoBinary and then 8-len(res)
    elif 0 < n < 128:
        res=numToBinary(n)
        return (8-len(res))*'0'+res
    # if not in range return error
    else:
        return "Error"
