'''
Created on Oct 24, 2018

@author: arana3 - Aparajita Rana

Pledge: I pledge my honor to abide by the Stevens Honor System - Aparajita Rana

CS115 - Hw 7
'''

def numToBaseB (N, B):
    #int converted to base B
    if N == 0:
        return ''
    elif N % B == 0:
        return numToBaseB (N//B, B) + '0'
    else:
        return numToBaseB ((N-N%B)//B, B) + str(N%B)
    
def baseBToNum (S, B):
    #base 10 same number
    if S == '':
        return 0
    else:
        return B*(baseBToNum (S[:-1],B)) + int(S[-1])

def baseToBase (B1, B2, SinB1):
    #a base (B1) & a base (B2) and a string representing a number in output a string representing the same number in base B2
    x = baseBToNum (SinB1, B1)
    return numToBaseB (x, B2)
  
def add (S, T):
    #Takes two binary strings returns binary sum
    x = baseBToNum (S, 2)
    y = baseBToNum (T, 2)
    return numToBaseB (x+y, 2)

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addB(S, T):
    # adds 2 binary string w/ dictionary
    def addbhelp(S,T, carry):
        if S=="" and T =="" and carry=="0":
            return ""
        if S=="" and T =="" and carry=="1":
            return "1"
        elif S=="":
            x= FullAdder[('0',T[-1],carry)]
        elif T=="":
            x= FullAdder[(S[-1],'0',carry)]
        else:
            x= FullAdder[(S[-1],T[-1],carry)]
        return addbhelp(S[:-1], T[:-1],x[1])+x[0]
    return addbhelp(S, T, "0")

# print(numToBaseB(4, 2))
# print(baseBToNum("11", 2))
# print(baseToBase(2, 10, "11"))
# print(add("11", "01"))
# print(addB("11", "1"))