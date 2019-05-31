'''
Created on Jan 27, 2015
Last modified on Feb 1, 2016
@author: Brian Borowski

CS115 - Functions returning functions
'''
import functools

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

def filter(function, iterable):
    '''filter(function, iterable) -> list
       Like list(filter(...)) in Python 3.'''
    return [item for item in iterable if function(item)] if function != None \
        else [item for item in iterable if item]

def reduce(function, iterable, initializer=None):
    return functools.reduce(function, iterable, initializer) \
        if initializer != None \
        else functools.reduce(function, iterable)

def div(k):
    '''Checks whether 42 is evenly divisible by an integer k.'''
    return 42 % k == 0

def divides(n):  # What does this do?
    def div(k):
        return n % k == 0
    return div

print(divides(100)(10))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def increment(n):
    '''Returns a function that takes in k and adds it to n.'''
    def add_n_to(k):
        return n+k
    return add_n_to

print(increment(10)(20))

def inc_all(nums, n):
    '''Add n to every number in a given list of numbers.'''
    return map(increment(n),nums)

def test_inc_all():
    '''Tests for inc_all. Correct tests print True.'''
    print(inc_all([], 2) == [])
    print(inc_all([1, 3, 5], 2) == [3, 5, 7])
    print(inc_all([-2, -1, 0, 1, 2], 10) == [8, 9, 10, 11, 12])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Another example involving functions that return functions.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
words = ['abate', 'abbey', 'abet', 'abhor', 'abide', 'able', 'ably',
         'about', 'above', 'abundant', 'abuse', 'abyss', 'ac', 'ace',
         'ache', 'achy', 'acid', 'acne', 'acorn', 'acre', 'acrid']

def make_len(n):
    '''Assume n is a non-negative integer. Return a function.
    That function applies to strings. It concatenates * characters
    to the given string, to make its length at least n.'''
    def pad_it(word):
        return word+('*'*(n-len(word)))
    return pad_it

def pad(words):
    return map(make_len(reduce(max, map(len, words))), words)
    '''Assume words is a non-empty list of strings. Let n be the
    length of the longest. Return a list of the same strings except
    with enough * characters appended to make each one length n.'''

def test_pad():
    '''Tests for pad. Correct tests print True.'''
    print(pad(['abate', 'abbey']) == ['abate', 'abbey'])  # no padding
    print(pad(['a', 'cat']) == ['a**', 'cat'])
    print(pad(['three', 'cats', 'asleep', 'now']) \
           == ['three*', 'cats**', 'asleep', 'now***'])

test_inc_all()
test_pad()
