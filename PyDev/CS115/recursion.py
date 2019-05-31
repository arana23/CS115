'''

'''
from cs115 import map, reduce, filter
import math
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def tower(n):
    """ Computer 2^(2^(2....)) using recursion """
    if n==0:
        return 1
    return 2**tower(n-1)

print(map(tower,range(6)))

def tower_reduce(n):
    def pow(x,y):
        return y**x
    return reduce(pow,[2]*n)

""" [1, 2, 3, 4] """
def length(lst):
    if lst  == []:
        return 0
    return 1+length(lst[1:])

def length_str(s):
    if s=='':
        return 0;
    return 1+length_str(s[1:])


def reverse(lst):
    if lst == []:
        return []
    return reverse(lst[1:])+[lst[0]]

def member(x, lst):
    #returns true if x is contained in the lsit and false otehrwise
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x,lst[1:])

print(member(1,[1,2,3]))

def collapse(lst):
    if lst == []:
        return []
    if isinstance(lst[0],list):
        return collapse(lst[0])+collapse(lst[1:])
    return [lst[0]+collapse(lst[1:])]

def my_map(f,lst):
    """returns a new lis where the function f has been applied to every element in the OG list"""
    if lst==[]:
        return []
    [f(lst[0])]+my_map(f, lst[1:])
    
def sqr(x):
    return x*x

def power(x,y):
    if(y==0):
        return 1
    return x * power(x, y-1)

def power_tail(x,y):
    def power_tail_helper(x, y, accum):
        if y==0:
            return accum
        return power_tail_helper(x, y-1, accum*x)
    return power_tail_helper(x, y, 1)

def my_reduce_helper(f, lst, accum):
    def my_reduce_helper(f, lst, accum):
        if(lst==[]):
            raise TypeError('my_reduce()')
    return my_reduce_helper(f, lst[1:], list[0])

# def prime(n):
#     possibleDivisors=range(2,int(math.sqrt(n)+1)
#     divisors=filter(lambda x: n % x==0, possible_divsors)
#     return len(divisors) == 0
# 
# def primes(n):
#     def sieve(lst):
#         if(lst==[]):
#             return []
#         return [lst[0]]+sieve(filter(lambda x: x%lst[0] != 0,lst[1:]))
#     return sieve(range(2, n+1))
#print(map(tower_reduce,range(1,5)))

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def subset(target, lst):
    ''' deteremines whether or not to create target sum using the values in the list can be 
    be positive, negative, or zero '''
    if target==0:
        return True
    if list==[]:
        return False
    return subset(target-lst[0], lst[1:]) or subset(target, lst[1:])
    
def powerset(lst):
    '''return the power set of the list, that is, the set of all subsets of the list'''
    if lst==[]:
        return [[]]
    #Lambda???
    #all of the lose_its first
    lose_it=powerset(lst[1:])
    use_it=map(lambda subset: [lst[0]]+subset, lose_it)
    return lose_it+use_it

    def subset_with_values(target,lst):
        """determines whether or not it is possible to create the target sum using val in the list
        the func returns a typle of exactly two items.first is a boolean that indicates true if the sum
        is possible and false if its not. the second element in the typle is a list of all the values that add
        up to make the target sum."""
        if target==0:
            return (True,[])
        if lst==[]:
            return (False, [])
        use_it=subset_with_values(target-lst[0], lst[1:])
        if use_it[0]:
            return (True, [lst[0]]+use_it[1])
        return subset_with_values(target, lst[1:])
    
    print(subset_with_values(5, [3,1,2]))
    
    def LCS(s1, s2):
        """returns the length of the longest common subsequence in string s1 & s2"""
        if s1== '' or s2== '':
            return 0
        if s1[0]==s2[0]:
            return 1+LCS(s1[1:], s2[1:])
        return max(LCS(s1,s2[1:]), LCS(s1[1:],s2)

# 
# print(LCS('spot','pot'))
# print(LCS('maps','spasm'))
# 
# def LCS_with_values(s1,s2):
#     if s1=='' or s2== '':
#         return [0, '']
#     if s1[0]==s2[0]:
#         result=LCS_with_values(s1[1:], s2[1:])
#         return [1+result[0], s1[0]+result[1]]
#     useS1=LCS_with_values(s1,s2[1:])
#     useS2=LCS_with_values(s1[1:],s2)
#     if(useS1[0]>useS2[0]):
#         return useS1
#     return useS2


    
    
    
    
