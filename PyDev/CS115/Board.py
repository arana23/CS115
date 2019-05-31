'''
Created on Dec 2, 2018

@author: Aparajita Rana
Pledge: I pledge my honor that I have abided by the Stevens Honor System - Aparajita Rana

'''
class Board(object):
    #constructor method -> initializes values 
    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        self.__board = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(' ')
            self.__board.append(row) 

    def __str__(self):
        #builds a board following init restraints
        result = ''
        for i in range(self.__height):
            a = '|'
            for j in range(self.__width):
                a += self.__board[i][j] +'|'
            a += '\n'
            result += a
        result += '-' * (self.__width * 2 + 1) + '\n'  
        for i in range(self.__width):
            result += ' ' + str(i)    
        return result
    
    def allowsMove(self, col):
        #returns true if allowed a move into column,returns false if not
        if col not in range(self.__width):
            return False
        return self.__board[0][col] == ' '
    
    def addMove(self, col, ox):
        #add an ox checker, where ox is a variable holding a string that is either "X" or "O", into column col
        for i in range(self.__height - 1, - 1, - 1):
            if self.__board[i][col] == ' ':
                self.__board[i][col] = ox
                break

    def setBoard(self, moveString):
        #takes in a string of columns and places alternating checkers, test your Connect-Four Board class
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
   
    def delMove(self, col):
        #opp of addMove, removes the top checker from the column
        for i in range(self.__height):
            if self.__board[i][col] != ' ':
                self.__board[i][col] = ' '
                break
            
    def winsFor(self, ox):
        #return True if the given checker, 'X' or 'O', held in ox, has won the calling Board
        for r in range(self.__height):
            for c in range(self.__width-3):
                if self.__board[r][c]==self.__board[r][c + 1]== self.__board[r][c + 2] == self.__board[r][c + 3] == ox:
                    return True
        for r in range(self.__height - 3):
            for c in range(self.__width):
                if self.__board[r][c] == self.__board[r + 1][c]== self.__board[r + 2][c] == self.__board[r + 3][c] == ox:
                    return True 
        for r in range(self.__height - 3):
            for c in range(self.__width - 3):
                if self.__board[r][c] == self.__board[r + 1][c + 1]== self.__board[r + 2][c + 2] == self.__board[r + 3][c + 3] == ox:
                    return True
        for r in range(self.__height - 3):
            for c in range(3, self.__width):
                if self.__board[r][c] == self.__board[r + 1][c - 1]== self.__board[r + 2][c - 2] == self.__board[r + 3][c - 3] == ox:
                    return True
        return False
    
    def hostGame(self):
        #loop to play game!
        print('Welcome to the game Connect Four!')
        player = 'O'
        while self.winsFor(player) == False:
            if player == 'O':
                player = 'X'    
            else:
                player = 'O'
            print(self)
            user = -1
            while self.allowsMove(user) == False:
                try:
                    user = int(input(player + "'s column choice: "))
                except:
                    print('Please enter a number 0-6')
            self.addMove(user, player)
        print(player + ' wins!')
        print(self)
        
b = Board( 7, 6 )
b.hostGame()