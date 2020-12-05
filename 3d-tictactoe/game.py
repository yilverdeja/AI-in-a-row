import math
import operator
from player import HumanPlayer, AIPlayer

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

        if self.isOutOfRange((0, coord[0], coord[1])): return False
        for layer in range(BOARD_SIZE):
            if self.board[layer][coord[0]][coord[1]] == " ":
                self.board[layer][coord[0]][coord[1]] = letter
                self.moves[letter].append((layer, coord[0], coord[1]))
                move = (layer, coord[0], coord[1])
                if self.checkWinner(move, letter):
                    self.winner = letter
                return True
        return False
    
    # Attempts to undo a move on the board
    def undoMove(self, coord, letter):
        self.__checkIfValidLetter(letter)

        if self.isOutOfRange((0, coord[0], coord[1])): return False
        # looks at the top most layer first
        for layer in range(2, -1, -1):
            if self.board[layer][coord[0]][coord[1]] == letter:
                self.board[layer][coord[0]][coord[1]] = " "
                self.moves[letter].remove((layer, coord[0], coord[1]))
                if self.winner != None:
                    self.winner = None
                return True
        return False
    
    def isOutOfRange(self, pos):
        # pos is (z, x, y)
        return pos[0] < 0 or pos[1] < 0 or pos[2] < 0 or pos[0] > BOARD_SIZE-1 or pos[1] > BOARD_SIZE-1 or pos[2] > BOARD_SIZE-1
    
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
        # checks last layer availability
        moves = set()
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[2][i][j] == " ":
                    moves.add((i, j))
        
        return list(moves)
    
    # checks if player has a 3 in a row
    def checkWinner(self, coord, letter):
        # coord is (x,y,z) aka (z, x, y) 
        # checks layer of coord (x, y)
        # checks diagonal through layers and vertical through layers
        vectors = [(0, -1, 0), (0, 0, -1), (0, -1,-1), (0, 1,-1), (1, 0, 0), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (1, 1, 1), (1,  1, -1), (1,  -1, 1), (1,  -1, -1)]
        for vector in vectors:
            lenCount = 1

            for a in range(1, BOARD_SIZE):
                head = (coord[0] + a*vector[0], coord[1] + a*vector[1], coord[2] + a*vector[2])
                if self.isOutOfRange(head) or self.board[head[0]][head[1]][head[2]] != letter:
                    break
                lenCount+=1
                if lenCount >= BOARD_SIZE:
                    return True

            for a in range(1, BOARD_SIZE):
                tail = (coord[0] - a*vector[0], coord[1] - a*vector[1], coord[2] - a*vector[2])
                if self.isOutOfRange(tail) or self.board[tail[0]][tail[1]][tail[2]] != letter:
                    break
                lenCount+=1
                if lenCount >= BOARD_SIZE:
                    return True

            if lenCount >= BOARD_SIZE:
                return True
        
        return False
        

    # Get's number of moves left, used for scoring
    def getNumMovesLeft(self):
        return int(math.pow(BOARD_SIZE, 3)) - len(self.moves["X"]) - len(self.moves["O"])

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

        # print("X score: ", game.getPlayerScore("X"))
        # print("O score: ", game.getPlayerScore("O"))
        
        game.printBoard()
        print(game.moves)

        # swap player
        letter = "X" if letter == "O" else "O"

    return

if __name__ == "__main__":
    g = Game()
    playerX = AIPlayer("X")
    playerO = HumanPlayer("O")
    play(g, playerX, playerO)

# if __name__ == "__main__":
    # playerX = HumanPlayer("X")
    # playerO = AIPlayer("O")
    # g = Game()
    # g.printBoard()
    # print(g.makeMove((0, 0), "X"))
    # print(g.makeMove((0, 0), "X"))
    # print(g.winner)
    # print(g.makeMove((0, 0), "X"))
    # print(g.winner)
    # print(g.makeMove((1, 1), "X"))
    # g.printBoard()
    # print(g.getPotentialMoves())
    # play(g, playerX, playerO)