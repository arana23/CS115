'''
Sep 20th, 2018

I pledge my honor that I have abided by the Stevens Honors System
@author Aparajita Rana
CS115 Lab - 3

'''
from cs115 import range

def change(amount, coins):
    #check if amount = 0, return 0 not possible
    if amount==0:
        return 0
    #check if list empty
    if coins==[]:
        return float("inf")
    #lose it, starts at '2nd' val
    lose_it=change(amount,coins[1:])
    if(amount<coins[0]):
        return lose_it
    #use it, adds one to value and calls another recursive message
    else:
        use_it=1+change(amount-coins[0], coins)
        return min(use_it,lose_it)
    
Dictionary = ['am','be'] 
#x=map(range(0,int(len(Dictionary)),Dictionary)
print(range(0,len(Dictionary)))
#print(change(48, [1, 5, 10, 25, 50]))