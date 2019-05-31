'''
Created on Sep 10, 2018

@author: Aparajita Rana
'''
def LCS(s1, s2):
    if s1== '' or s2== '':
        return 0
    # checks of the first position of the two variables are equal 
    if s1[0]==s2[0]:
        return 1+LCS(s1[1:], s2[1:])
    return max(LCS(s1,s2[1:]), LCS(s1[1:],s2)

print(LCS('ACT','AT'))