'''
Created on September 17, 2018
@author:   Kishan Patel, Aparajita Rana
username: kpate79
username: arana3
Pledge:  I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10],]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

def letterScore(letter, scorelist):
    """Finds the appropriate amount of points a letter is worth from the give key "scorelist" """
    if scorelist == []:
        return None
    if letter in scorelist[0]:
        return scorelist[0][1]
    return letterScore(letter,scorelist[1:])

def wordScore(S,scorelist):
    """Finds the amount of points a certain word is worth based on the points of each letter derived from the function
    letterScore"""
    if S == '' or scorelist == []:
        return 0
    return letterScore (S[0], scorelist) + wordScore (S[1:], scorelist)

def scoreList(Rack):
    """Takes an input of a "Rack" of letters and finds which words can be produced from Dictionary, 
    and also returns the points for each word."""
    
    def wordLetters(S, Rack, n):
        """Takes inputs of a string "S" and the letters in "Rack", as well as a variable n, and returns Boolean True, 
        if the letters from Rack match S up to S[n]. It makes sure there are enough letters in Rack to form string S.""" 
        if n == len(S): return True
        if S[n] in Rack:
            if len (filter (lambda x: S[n] == x, S)) <= len (filter (lambda x: S[n] == x, Rack)): 
                return True and wordLetters(S, Rack, n+1)
            else: 
                return False        
    def wordChecker(Rack):
        """Takes an input of a "Rack" of letters and returns a list of words that can be formed"""
        def wordCheckerHelper(S):         
            if (lambda x: x in Rack, S):
                if wordLetters(S, Rack, 0):
                    return [S] + [wordScore (S, scrabbleScores)]
                else:
                    return []
            else:
                return []
        return wordCheckerHelper
    return filter (lambda a: a != [], map (wordChecker (Rack), Dictionary))
        
def bestWord(Rack):
    """Takes in put of a list of letters "Rack" and returns the word with the highest score"""
    def bestHelper(w1,w2):
        if w2 == []:
            return w1
        if w2[0][1] > w1[1]:
            w1 = w2[0]
            return bestHelper(w1, w2[1:])
        else:
            return bestHelper(w1, w2[1:])
    if scoreList(Rack) == []:
        return ["",0]
    return bestHelper(scoreList(Rack)[0], scoreList(Rack)) 


