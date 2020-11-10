import math
import time

from player import HumanPlayer, RandomPlayer, AIPlayer

BOARD_SIZE = 3

diag1 = [(BOARD_SIZE-1)*i for i in range(1, BOARD_SIZE+1)]

diag2Diff = int((math.pow(BOARD_SIZE, 2) - 1)/(BOARD_SIZE-1))
diag2 = [diag2Diff*i for i in range(BOARD_SIZE)]

class Game():
    def __init__(self):
        self.board = self.makeBoard()
        self.winner = None
    
    @staticmethod
    def makeBoard():
        return [str(i) for i in range(int(math.pow(BOARD_SIZE, 2)))]
    
    def printBoard(self):
        for row in [self.board[i*BOARD_SIZE:(i+1) * BOARD_SIZE] for i in range(BOARD_SIZE)]:
            print('| ' + ' | '.join(row) + ' |')

    def makeMove(self, coord, letter):
        if isInt(self.board[coord]):
            self.board[coord] = letter
            if self.checkWinner(coord, letter):
                self.winner = letter
                # print("winner is: ", self.winner)
            return True
        return False
    
    def undoMove(self, coord, letter):
        if self.checkWinner(coord, letter):
            self.winner = None
        self.board[coord] = str(coord)
    
    def checkWinner(self, coord, letter):
        rowIndex = math.floor(coord/BOARD_SIZE)
        row = self.board[rowIndex*BOARD_SIZE:(rowIndex+1)*BOARD_SIZE]
        # print("row: ", row)
        if all([c == letter for c in row]):
            return True
        
        colIndex = coord % BOARD_SIZE
        col = [self.board[colIndex+(i*BOARD_SIZE)] for i in range(BOARD_SIZE)]
        # print("col: ", col)
        if all([c == letter for c in col]):
            return True
        
        diagonal1 = [self.board[i] for i in diag1]
        if all([c == letter for c in diagonal1]):
            return True

        diagonal2 = [self.board[i] for i in diag2]
        if all([c == letter for c in diagonal2]):
            return True

        return False
    
    def getAvailableCoords(self):
        coords = []
        for i in range(int(math.pow(BOARD_SIZE, 2))):
            if isInt(self.board[i]):
                coords.append(i)
        return coords
    
    def isBoardEmpty(self):
        return len(self.getAvailableCoords()) == int(math.pow(BOARD_SIZE, 2))
    
    def getCornerCoords(self):
        return [0, BOARD_SIZE-1, BOARD_SIZE*(BOARD_SIZE-1), int(math.pow(BOARD_SIZE, 2))-1]

def play(game, playerX, playerO):
    game.printBoard()

    letter = "X"

    while game.winner == None and len(game.getAvailableCoords()) > 0:
        if letter == "X":
            playerX.makeMove(game)
        else:
            playerO.makeMove(game)

        print("Made move for: ", letter)
        game.printBoard()
    
        # swap player
        letter = "O" if letter == "X" else "X"
        time.sleep(0.5)
        
    print("Winner is: ", game.winner)
    print("Game Over")
    if (game.winner == None):
        print("It's a tie!")

def isInt(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    playerX = AIPlayer("X")
    playerO = AIPlayer("O")
    g = Game()
    play(g, playerX, playerO)