'''
Created on 10/07/18
@author:   arana3 - Aparajita Rana
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - Aparajita Rana

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.
turtle.left(90)
turtle.color("green")
turtle.color()
turtle.pensize(3)

def sv_tree(trunk_length, levels):
    #if the levels have all been fufilled then stop running the else loop
    if levels == 0:
        return "completed"
    else:
        #moves forward the trunk length -> val changes after the call again on line 21
        turtle.forward(trunk_length)
        turtle.left(45)
        #other part of branch 
        sv_tree(trunk_length/2,levels-1)
        turtle.right(45)
        #in order to return to original location
        turtle.backward(trunk_length)
        turtle.forward(trunk_length)
        turtle.right(45)
        #other side of branch
        sv_tree(trunk_length/2,levels-1)
        turtle.left(45)
        turtle.backward(trunk_length)

def fast_lucas(n):
    #follows same pattern as the memo fib only base cases are changed
    def lucas_helper(n, memo):
        if n in memo:
            return memo[n]
        #base cases (elif not required) lucas number starts with 2, so first int is 2
        if n==0:
            result=2
        elif n==1:
            result=1
        else:
            #calculation of the next lucas number
            result= lucas_helper(n-1,memo)+lucas_helper(n-2, memo)
        memo[n]=result
        return result
    return lucas_helper(n, {})

    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
      # TODO

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if((amount,coins) in memo):
            return memo[amount,coins]
        #base cases checking if amount and coins are valid inputs
        if amount==0:
            result=0
        elif coins == () or amount <0:
            result= float("inf")
        else:
            #useit and loseit comparable to givechange, calls helper method 
            useit=1+fast_change_helper(amount-coins[0], coins, memo)
            result=min(useit, fast_change_helper(amount, coins[1:], memo))
            memo[amount,coins]=result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(50, 6)