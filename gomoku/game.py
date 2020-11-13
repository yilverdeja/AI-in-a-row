import math
from player import HumanPlayer

BOARD_SIZE = 15

class Game():

    def __init__(self):
        self.board = self.makeBoard()
        self.winner = None
    
    # Makes the 15x15 board to play Gomoku
    @staticmethod
    def makeBoard():
        return [[" " for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
    # prints a 15x15 board
    def printBoard(self):
        for i in range(BOARD_SIZE):
            print('| ' + ' | '.join(self.board[i]) + ' |')
                
    # Attempts to make a move on the board
    def makeMove(self, coord, letter):
        if (self.board[coord[0]][coord[1]] == " "):
            self.board[coord[0]][coord[1]] = letter
            # TODO: check winner?
            return True
        return False
    
    # Attempts to undo a move on the board
    def undoMove(self, coord, letter):
        if (self.board[coord[0]][coord[1]] == letter):
            self.board[coord[0]][coord[1]] = " "
            if self.winner != None:
                self.winner = None
            return True
        return False
    
# plays the game
def play(game, playerX, playerY):
    game.printBoard()

    letter = "X"
    
    # TODO: or no more available coords
    while game.winner == None:
        print("Player "+letter+" move")
        if letter == "X":
            playerX.makeMove(game)
        else:
            playerO.makeMove(game)
        
        game.printBoard()

        # swap player
        letter = "X" if letter == "O" else "O"

    return

if __name__ == "__main__":
    g = Game()
    playerX = HumanPlayer("X")
    playerO = HumanPlayer("O")
    play(g, playerX, playerO)
    
    
