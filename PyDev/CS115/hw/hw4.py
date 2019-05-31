'''
October 1st, 2018

I pledge my honor that I have abided by the Stevens Honors System

@author arana3 - Aparajita Rana
CS115 HW - 4

'''
def pascal_row(n):
    """prints a list of elements found in a n row of Pascal's Triangle"""
    #if not valid n return empty list
    if n<0:
        return []
    #base case
    if n==0:
        return[1]
    #temp variable -> 
    else:
        a=pascal_row(n-1)
        return [1]+list(map(lambda x:a[x]+a[x+1],range(len(a)-1)))+[1]

def pascal_triangle (n):
    """takes input n and returns a list of lists containing
    values of rows including row n"""
    #if not valid n, return empty list of lists
    if n<0:
        return [[]]
    #base case
    if n==0:
        return[[1]]
    else:
        return pascal_triangle(n-1)+[pascal_row(n)]