'''
Created on Oct 31, 2018

@author: arana3
'''

def shallow_copy(lst):
    new_list=[]
    for x in lst:
        new_list.append(x)
    return new_list

def shallow_copy_list_comprehension(lst):
    return [x for x in lst]

L = [1, 2, [3, [4, 5]]]
M= shallow_copy_list_comprehension(L)
L[2]=4
print(M)
print(L)

def deep_copy(lst):
    new_list=[]
    for x in lst:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list
L=[1, 2, [3, [4, 5]]]
M=deep_copy(L)
L[2][1][0]=14
print(M)
print(L)


