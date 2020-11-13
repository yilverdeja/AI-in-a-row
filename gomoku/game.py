import math

BOARD_SIZE = 15

class Game():

    def __init__(self):
        self.board = self.makeBoard()
        self.winner = None
    
    # Makes the 15x15 board to play Gomoku
    @staticmethod
    def makeBoard():
        return [[None for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
    # prints a 15x15 board
    def printBoard(self):
        pass
                
    # Attempts to make a move on the board
    def makeMove(self, coord, letter):
        if (self.board[coord[0]][coord[1]] == None):
            self.board[coord[0]][coord[1]] = letter
            # TODO: check winner?
            return True
        return False
    
    # Attempts to undo a move on the board
    def undoMove(self, coord, letter):
        if (self.board[coord[0]][coord[1]] == letter):
            self.board[coord[0]][coord[1]] = None
            if self.winner != None:
                self.winner = None
            return True
        return False
    
# plays the game
def play(game):
    game.printBoard()
    # coord = (0,0)
    # if game.makeMove(coord, "X"):
    #     print("move success")
    # print(game.board)
    # if game.undoMove(coord, "X"):
    #     print("undo success")
    # print(game.board)
    return

if __name__ == "__main__":
    g = Game()
    play(g)
    
    
