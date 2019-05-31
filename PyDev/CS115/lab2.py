'''
Sep 13th, 2018

I pledge my honor that I have abided by the Stevens Honors System
@author Aparajita Rana
CS115 Lab - 2

'''

def length_str(s):
    """given s, returns the length of s with empty s as base case"""
    if s==[]:
        return 0
    elif s=='':
        return 0
    return 1+length_str(s[1:])

def dot(L,K):
    """if two vals lengths arent equal dot can't be done return 0.0"""
    #if two vals lengths are zero dot can't be done return 0.0
    if(length_str(L)==0 or length_str(K)==0):
        return 0.0
    #return first vals multiplied and then every corresponding val from there
    return L[0]*K[0]+dot(L[1:],K[1:])

def explode(S):
    #if the length is zero return empty []
    if(length_str(S)==0):
        return []
    #return first val and then every other value seperately
    return [S[0]] + explode(S[1:])

def ind(e,L):
    if L == [] or L == "" or e == L[0]:
    #if e is equal to L at 0, return 0
        return 0    
    return 1+ind(e,L[1:])

def removeAll(e,L):
    #check for empty string/list lines 47 & 49
    if (L==[]):
        return L
    elif(L==''):
        return L
    else:
        # check if e is equal to L at 0, if not return val including L[0]
        if e != L[0]:
            return [L[0]] + removeAll (e, L[1:])
        else:
            #otherwise don't include L[0]
            return removeAll (e, L[1:])
        
def even(X):
    #check if mod 2 ==0 -> an even number, return true
    if X % 2 == 0: 
        return True
    else:
        #if not, its odd return false
        return False
    
def myFilter(f,L):
    #check for empty/last element
    if L==[]:
        return []
    #check the sub zero value if true bc not tested
    if(f(L[0])):
        #return first val since true plus the remaining calls of myFilter
        return [L[0]]+myFilter(f, L[1:])
            #since sub zero val isn't fulfilling, print rest of calls 
    return myFilter(f,L[1:])

def deepReverse(L):
    if(L==[]):
        return []
    else:
        # IFcheck if a list??? at L[0]
        if(isinstance(L[0],list)):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
            # L[0] is not a list, add to the end
        else:
            return deepReverse(L[1:]) + [L[0]]