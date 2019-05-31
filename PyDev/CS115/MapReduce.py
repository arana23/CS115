'''
Crated on Sep 2018
@author: Aparajita
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

if __name__ == '__main__':
    print(range(0, 10, 2))
    print(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))
    print(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))


def add(x,y):
    return x+y

def sqr(x):
    return x*x

def mult(x,y):
    return x*y

def span(lst):
    "Returns the difference between the maximum and minimum numebers in a list"
    return reduce(max, lst) - reduce(min, lst)

print(span([3, 1, 42, 7]))
print(span([42, 42, 42, 42]))

def gauss(n):
    "takes as input a positive integer n and returns the sum 1 + 2 + 3 + 4 + ... + n"
    return reduce(add, range(1, n+1))

print(gauss(10))

def sum_of_squares(n):
    "1^2 + 2^2 + 3^2 + .... + n^2"
    return reduce(map(sqr,range(1, n+1)))

list_of_ints = [1, 2, 3, 4, 5]
print(reduce(mult, list_of_ints))

list_of_strings = ['hello', 'my', 'name', 'is', 'brian']
print(map(len, list_of_strings))
print(reduce(map(len, list_of_strings)))

def coin_row(lst):
    if lst==[]:
        return 0
    return max(lst[0]+coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    if lst==[]:
        return [0,[]]
    use_it=coin_row_with_values(lst[2:])
    new_sum=lst[0]+use_it[0]
    lose_it=coin_row_with_values(lst[1:])
    if(new_sum>lose_it[0]):
        return [new_sum,[lst[0]+use_it[1]]]    
    return lose_it

def distance(first, second):
    if first=='':
        return len(second)
    if second=='':
        return len(first)
    if first[0]==second[0]:
        return distance(first[1:],second[1:])
    #substitution=distance
"""print(sum_of_squares(3))"""