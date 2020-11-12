import math
import time

from player import HumanPlayer, RandomPlayer, AIPlayer

BOARD_SIZE = 5

diag1 = [(BOARD_SIZE-1)*i for i in range(1, BOARD_SIZE+1)]

diag2Diff = int((math.pow(BOARD_SIZE, 2) - 1)/(BOARD_SIZE-1))
diag2 = [diag2Diff*i for i in range(BOARD_SIZE)]

coordPlays = {"X": [], "O": []}

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
            return True
        return False
    
    def undoMove(self, coord, letter):
        if self.checkWinner(coord, letter):
            self.winner = None
        self.board[coord] = str(coord)
    
    def checkWinner(self, coord, letter):
        rowIndex = math.floor(coord/BOARD_SIZE)
        row = self.board[rowIndex*BOARD_SIZE:(rowIndex+1)*BOARD_SIZE]
        if all([c == letter for c in row]):
            return True
        
        colIndex = coord % BOARD_SIZE
        col = [self.board[colIndex+(i*BOARD_SIZE)] for i in range(BOARD_SIZE)]
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
    
    def getAvailableCoordsInProximity(self):
        coords = set()
        for i in range(int(math.pow(BOARD_SIZE, 2))):
            if not isInt(self.board[i]):
                coords.update(self.getSideCoords(i))
        
        return list(coords)
    
    def getSideCoords(self, coord):
        coords = []

        coords.append(coord + BOARD_SIZE)
        coords.append(coord - BOARD_SIZE)
        if coord % BOARD_SIZE != 0:
            coords.append(coord - 1)
            coords.append(coord + BOARD_SIZE - 1)
            coords.append(coord - BOARD_SIZE - 1)
        if (coord + 1) % BOARD_SIZE != 0:
            coords.append(coord + 1)
            coords.append(coord + BOARD_SIZE + 1)
            coords.append(coord - BOARD_SIZE + 1)
        
        finalCoords = []
        for c in coords:
            
            if c >= 0 and c < int(math.pow(BOARD_SIZE, 2)) and isInt(self.board[c]):
                finalCoords.append(c)
        
        # print("Side Coords: ", finalCoords)
        return finalCoords
    
    def isBoardEmpty(self):
        return len(self.getAvailableCoords()) == int(math.pow(BOARD_SIZE, 2))
    
    def getCornerCoords(self):
        return [0, BOARD_SIZE-1, BOARD_SIZE*(BOARD_SIZE-1), int(math.pow(BOARD_SIZE, 2))-1]

def play(game, playerX, playerO):
    game.printBoard()

    letter = "X"

    while game.winner == None and len(game.getAvailableCoords()) > 0:
        if letter == "X":
            coord = playerX.makeMove(game)
        else:
            coord = playerO.makeMove(game)
        
        
        coordPlays[letter].append(coord)
        game.getSideCoords(coord)

        print(game.getAvailableCoordsInProximity())

        print("Made move for: ", letter)
        game.printBoard()
    
        # swap player
        letter = "O" if letter == "X" else "X"

        # Wait
        time.sleep(0.5)
        
    print("Winner is: ", game.winner)
    print("Game Over")
    if (game.winner == None):
        print("It's a tie!")

# Checks if the value is an integer
def isInt(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    playerX = HumanPlayer("X")
    playerO = AIPlayer("O")
    g = Game()
    play(g, playerX, playerO)