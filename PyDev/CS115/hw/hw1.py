'''
Sep 10th, 2018

I pledge my honor that I have abided by the Stevens Honors System
@author Aparajita Rana
CS115 HW-1 

'''
from cs115 import map, reduce

def mult(x, y):
    """Returns the product of x and y"""
    return x * y

print(reduce(mult, [2, 3]))

def factorial(n):
    """range from 1 to n value is equivalent to the ! then the mult and reduce
    allows for each value to be multiplied by one another"""
    return reduce(mult, range(1,n+1))

def add(x,y):
    """adds two variables"""
    return x+y

def mean(n):
    """calculates the mean of the list of numbers given in n"""
    """reduce adds together each value in n and len(n) divides by the length"""
    return (reduce(add,n))/len(n)

def divides(n):
    """returns div -> true/false based on the equation of div(k), k is the 2nd variable given when calling divides(n)"""
    def div(k):
        return n % k == 0
    return div

def sum(n):
    """ adds together all values in n list"""
    return reduce(add,n)

def prime(n):
    """utilizes the divides(n)(k) for k= every value in the range(2,n), stores
    result in map. If all values in the map were false sum(map of false)==0, returns
    true. Otherwise, if there was even one instance where n was divisible it's !=0 returns false"""
    #print(map(divides(n),range(2,n)))
    return sum(map(divides(n),range(2,n)))==0
