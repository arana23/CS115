'''
Created on 9/25/18
@author:   @arana3 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System 

CS115 - Hw 3
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from hw2 import wordScore
# your code goes here
def giveChange(amount,coins):
    #if no amount, return empty list of empty list
    if amount==0:
        return[0,[]]
    elif coins==[]:
        return[float("inf"),[]]
    elif coins[0]>amount:
        return giveChange(amount,coins[1:])
    #use it subtracts total amount from first coins val
    #lose it recursive amount and coins without first val
    useIt=giveChange(amount-coins[0],coins)
    loseIt=giveChange(amount,coins[1:])
    if useIt[0]<loseIt[0]:
        return[1+useIt[0],[coins[0]]+useIt[1]] 
    else:
        return loseIt
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordLetters(S, Rack, n):
        """Takes inputs of a string "S" and the letters in "Rack", as well as a variable n, and returns Boolean True, 
        if the letters from Rack match S up to S[n]. It makes sure there are enough letters in Rack to form string S.""" 
        #check if len(S) is equiv to n
        if n==len(S): 
            return True
        #check if S[n] is in Rack
        if S[n] in Rack:
            if len(filter(lambda x: S[n]== x,S)) <= len(filter(lambda x: S[n]==x,Rack)): 
                return True and wordLetters(S,Rack,n+1)
            else: 
                return False
    
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]'''
    #lambda returns wordscore, map returns the total list of wordscore
    return list(map(lambda x:[x,wordScore(x,scores)],dct))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    #if empty return empty list
    if n==0 or L==[]:
        return []
    #slice and listify first L element
    return [L[0]]+take(n-1,L[1:])
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    #check empty
    if L==[]:
        return []
    #if at n=0, return the L val
    if n==0:
        return L   
    return drop(n-1,L[1:])