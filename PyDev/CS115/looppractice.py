'''
Created on Oct 29, 2018

@author: arana3
'''

def map_sqr(lst):
    result=[]
    for x in lst:
        result.append(x**2)
    return result

def map_sqr_list_compre(lst):
    """Assume lst is a list, return map(sqr, lst)"""
    return [x*x for x in lst]

def find_max(lst):
    if lst==[]:
        return None
    maxv=lst[0]
    for x in lst:
        if x>=maxv:
            maxv=x
    return maxv

def find_max_min(lst):
    if lst==[]:
        return None
    maxv=lst[0]
    minv=lst[0]
    for x in lst:
        if x>maxv:
            maxv=x
        elif x<minv:
            minv=x 
    return [maxv, minv]   

print(find_max_min([2,2,2]))
print(map_sqr_list_compre([1,2,3]))