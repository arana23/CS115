#
# life.py - Game of Life lab
#
# Name: arana3 - Aparajita Rana
# Pledge: I pledge my honor that I have abided by the Stevens Honor System - Aparajita Rana
#
import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
#"""returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        temp=list(map(lambda x:0,range(width)))
        A += [temp] # What do you need to add a whole row here?
    return A

def printBoard(A):
#this function prints the 2d list-of-lists
#A without spaces (using sys.stdout.write)
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    #except first and last line and border make inner cells 1
    A=createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1:
                A[row][col]=0
            else:
                A[row][col]=1
    return A        

def randomCells(w,h):
    #randomly assign 1s and 0s to places
    A=createBoard(w,h)
    for row in range(h):
        for col in range(w):
            A[row][col]=random.choice([0,1])
    return A

def copy(A):
    #deeep copy that
    copied=createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            copied[row][col]=A[row][col]
    return copied

def innerReverse(A):
    copied=createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row==0 or col==0 or row==len(A)-1 or col==len(A[0])-1:
                copied[row][col]=0
            elif A[row][col]==0:
                copied[row][col]=1
            else:
                copied[row][col]=0
    return copied

def countNeighbors(row,col, A):
    neighbors = 0
    if A[row+1][col] == 1:
        neighbors += 1
    if A[row][col+1] == 1:
        neighbors += 1
    if A[row-1][col] == 1:
        neighbors += 1
    if A[row][col-1] == 1:
        neighbors += 1
    if A[row+1][col+1] == 1:
        neighbors += 1
    if A[row-1][col-1] == 1:
        neighbors += 1
    if A[row-1][col+1] == 1:
        neighbors += 1
    if A[row+1][col-1] == 1:
        neighbors += 1
    return neighbors

def next_life_generation(A):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0."""
    newa = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == 0 or row == (len(A) - 1) or col == 0 or col == (len(A[0]) - 1):
                A[row][col] = 0
            elif countNeighbors(row, col, A) < 2:
                newa[row][col] = 0
            elif countNeighbors(row, col, A) > 3:
                newa[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                newa[row][col] = 1
            else:
                newa[row][col] = A[row][col]  
    return newa

A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
printBoard(A)
print()
A2 = next_life_generation(A)
printBoard(A2)