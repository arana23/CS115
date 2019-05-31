'''
Created on Oct 16, 2018

@author: arana3 - Aparajita Rana

Pledge: I pledge my honor to abide by the Stevens Honor System - Aparajita Rana

CS115 - Hw 6
'''
from CS115 import lab6 
from CS115.lab6 import numToBinary
from lab6 import count, binaryToNum
from CS115.cs115 import reduce

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#I have attached my binarytoNum bc of import above^
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


def counting(S,n):
    #counts how many times the number occurs in list S.'''
    if S == '':
        return 0
    if S[0]!= n:
        return 0
    return 1+ counting(S[1:],n)

def zeroify(x):
    # 5 zeros before binary number
    return (COMPRESSED_BLOCK_SIZE-len(x))*"0"+x 

def compress(S):
    #returns a run-length encoding of the binary 64 input
    def compress_helper(S,count):
        if S == '':
            return '' 
        num = counting(S,count)
        if num >MAX_RUN_LENGTH:
            num = MAX_RUN_LENGTH
        return zeroify(numToBinary(num)) + compress_helper(S[num:], str(1-(int(count))))
    return compress_helper(S,'0')

def uncompress(C):
    #Takes in the run-length encoding of S return binary, reverse of above
    def uncompress_helper(C,count):
        if C =='':
            return ''
        return binaryToNum(C[:COMPRESSED_BLOCK_SIZE]) * count + uncompress_helper(C[COMPRESSED_BLOCK_SIZE:], str(1-int(count)))
    return uncompress_helper(C,'0')

def compression(S):
    #ratio of compressed to uncompressed
    return len(compress(S))/(len(S)*1.0)