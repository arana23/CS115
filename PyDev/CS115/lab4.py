'''
Sep 27th, 2018

I pledge my honor that I have abided by the Stevens Honors System
@author arana3 - Aparajita Rana
CS115 Lab - 4

'''
def knapsack(capacity, itemList):
    if itemList==[] or capacity==0:
        return [0,[]]
    elif itemList[0][0]>capacity:
        return knapsack(capacity,itemList[1:])
    useit=knapsack(capacity-itemList[0][0],itemList[1:])
    loseit=knapsack(capacity,itemList[1:])
    if itemList[0][1]+useit[0]>loseit[0]:
        return [itemList[0][1]+useit[0],[itemList[0]]+useit[1]]
    return loseit