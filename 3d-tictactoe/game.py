import math
import operator
# from player import HumanPlayer

BOARD_SIZE = 3

class Game():

    def __init__(self):
        self.board = self.makeBoard()
        # self.moves = {"X": [], "O": []}
        self.winner = None
    
    # Makes the 3x3x3 board to play 3D Tic Tac Toe
    @staticmethod
    def makeBoard():
        return [[[" " for k in range(BOARD_SIZE)] for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

if __name__ == "__main__":
    # playerX = HumanPlayer("X")
    # playerO = AIPlayer("O")
    g = Game()
    print(g.board)
    # play(g, playerX, playerO)