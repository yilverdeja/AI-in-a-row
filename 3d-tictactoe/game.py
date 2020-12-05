import math
import operator
# from player import HumanPlayer

BOARD_SIZE = 3

class Game():

    def __init__(self):
        self.board = self.makeBoard()
        self.moves = {"X": [], "O": []}
        self.winner = None
    
    # Makes the 3x3x3 board to play 3D Tic Tac Toe
    @staticmethod
    def makeBoard():
        return [[[" " for k in range(BOARD_SIZE)] for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
    # prints a 3x3x3 board
    def printBoard(self):
        for j in range(BOARD_SIZE):
            print(j+1)
            for i in range(BOARD_SIZE):
                print('| ' + ' | '.join(self.board[j][i]) + ' |')
    
    def makeMove(self, coord, letter):
        # coord is an x, y position
        # a move can only be made within the board and if there's a piece below it (next layer)
        # checks coord at lowest layer, if unavailable moves up layer and checks until last layer
        self.__checkIfValidLetter(letter)

        if self.isOutOfRange(coord): return False
        for layer in range(BOARD_SIZE):
            if self.board[layer][coord[0]][coord[1]] == " ":
                self.board[layer][coord[0]][coord[1]] = letter
                self.moves[letter].append((layer, coord[0], coord[1]))
                # check winner
                return True
        return False
    
    # Attempts to undo a move on the board
    def undoMove(self, coord, letter):
        self.__checkIfValidLetter(letter)

        if self.isOutOfRange(coord): return False
        for layer in range(BOARD_SIZE):
            if self.board[layer][coord[0]][coord[1]] == letter:
                self.board[layer][coord[0]][coord[1]] = " "
                self.moves[letter].remove((layer, coord[0], coord[1]))
                if self.winner != None:
                    self.winner = None
                return True
        return False
    
    def isOutOfRange(self, pos):
        return pos[0] < 0 or pos[1] < 0 or pos[0] > BOARD_SIZE-1 or pos[1] > BOARD_SIZE-1
    
    # private function to check if the letter is either X or O
    def __checkIfValidLetter(self, letter):
        if letter != "X" and letter != "O":
            raise Exception("Input letter must either be X or O!")

    # checks if board is empty
    def isBoardEmpty(self):
        return len(self.moves["X"]) == 0 and len(self.moves["O"]) == 0
    
    # checks if the board is full
    def isBoardFull(self):
        return len(self.moves["X"]) + len(self.moves["O"]) >= int(math.pow(BOARD_SIZE, 3))
    
    def getPotentialMoves(self):
        # goes through every layer starting at the bottom, checks every open move and checks if above has a piece or not
        moves = set()
        

if __name__ == "__main__":
    # playerX = HumanPlayer("X")
    # playerO = AIPlayer("O")
    g = Game()
    g.printBoard()
    print(g.makeMove((0, 0), "X"))
    print(g.makeMove((0, 0), "X"))
    print(g.makeMove((0, 0), "X"))
    print(g.makeMove((1, 1), "X"))
    g.printBoard()
    # play(g, playerX, playerO)