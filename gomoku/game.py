import math
import operator
from player import HumanPlayer, AIPlayer

# TODO: don't hardcode in player.py
BOARD_SIZE = 15

# Shows all open "in a row moves". Every dictionary holds in array of tuple arrays i.e [[(), ()], [(), (), ()]]
# c# is a closed combo which means one side is blocked and you only need one play to block it completely
xMoves = {"4": [], "c4": [], "3": [], "c3": [], "2": [], "c2": [], "blocked": []}
oMoves = {"4": [], "c4": [], "3": [], "c3": [], "2": [], "c2": [], "blocked": []}

class Game():

    def __init__(self):
        self.board = self.makeBoard()
        self.moves = {"X": [], "O": []}
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
        if self.isOutOfRange(coord): return False
        if (self.board[coord[0]][coord[1]] == " "):
            self.board[coord[0]][coord[1]] = letter
            self.moves[letter].append(coord)
            # TODO: check winner?
            return True
        return False
    
    # Attempts to undo a move on the board
    def undoMove(self, coord, letter):
        if self.isOutOfRange(coord): return False
        if (self.board[coord[0]][coord[1]] == letter):
            self.moves[letter].remove(coord)
            self.board[coord[0]][coord[1]] = " "
            if self.winner != None:
                self.winner = None
            return True
        return False
    
    # checks if board is empty
    def isBoardEmpty(self):
        return len(self.moves["X"]) == 0 and len(self.moves["O"]) == 0
    
    # checks if the board is full
    def isBoardFull(self):
        return len(self.moves["X"]) + len(self.moves["O"]) >= int(math.pow(BOARD_SIZE, 2))
    
    # gets the number of positions left on the board
    def getNumPosLeft(self):
        return int(math.pow(BOARD_SIZE, 2)) - len(self.moves["X"]) - len(self.moves["O"])
    
    # def getPlayerScore(self, letter):
    #     # TODO is there a better way to simplify this
    #     if letter == "X":
    #         return 1000*len(xMoves["4"]) + 100*len(xMoves["c4"]) + 50*len(xMoves["3"]) + 25*len(xMoves["c3"]) + 10*len(xMoves["2"]) + 5*len(xMoves["c2"])
    #     elif letter == "O":
    #         return 1000*len(oMoves["4"]) + 100*len(oMoves["c4"]) + 50*len(oMoves["3"]) + 25*len(oMoves["c3"]) + 10*len(oMoves["2"]) + 5*len(oMoves["c2"])
    
    # # TODO
    # def updateXMoves(self, pos):
    #     # look through all current xMoves and check next to their rows if pos exists there. If so, then remove it from the in-a-row dic value and add it to the next one
    #     for item in xMoves.items():
    #         # TODO add if block into helper function to be used by updateOMoves
    #         # TODO this currently assumes a straight line, what if there's a single break between a series i.e (0,1), (0,2), (0,4); This is basically a 3 in a row. A (0,3) can be placed to make a 4 in a row
    #         if len(item[0]) > 0:
    #             if item[0] == "c2":
    #                 # [[(0, 1), (0, 2)], [(4,4), (5,4)]]
    #                 # for first one it searches if pos is at (0,0), (0,3) or (0,4)
    #                 # for second one it searches if pos is at (2, 4), (3, 4), (6,4), (7,4)
    #                 # if it is, then it removes this item from c2 and adds it into c3
                    
    #                 # each should have at least 2 points which helps determine the direction
    #                 for comb in item[1]:
    #                     directionVector = self.getDirection(comb[0], comb[1])
    #                     # get current head and tail and look one pos next to them
    #                     # when heading to the right of the comb, add by -1*direction
    #                     # else add by 1*direction
    #                     head = tuple(map(operator.add, comb[0], directionVector))
    #                     tail = tuple(map(operator.add, comb[-1], -1*directionVector))

    #                     # add pos into comb, add it into c3 then remove comb from c2 item
    #                     if head == pos:
    #                         comb.insert(0, pos)
    #                         xMoves["c3"].append(comb)
    #                         item[1].remove(comb)
    #                     elif tail == pos:
    #                         comb.append(pos)
    #                         xMoves["c3"].append(comb)
    #                         item[1].remove(comb)
                    
    #             elif item[0] == "2":
    #                 pass
    #             elif item[0] == "c3":
    #                 pass
    #             elif item[0] == "3":
    #                 pass
    #             elif item[0] == "c4":
    #                 pass
    #             elif item[0] == "4":
    #                 pass
    #             else:
    #                 raise Exception("Shouldn't arrive here!")
    #     pass

    def getDirection(self, t1, t2):
        # https://www.geeksforgeeks.org/python-how-to-get-subtraction-of-tuples/
        return tuple(map(operator.sub, t1, t2))

    def updateOMoves(self, pos):
        pass

    def getPotentialMoves(self, dist):
        moveSet = set()
        if dist == 1:
            vectors = [(1, 0), (0, 1), (1,1), (1,-1)]
        else:
            vectors = [(-1, 0), (0, -1), (-1,-1), (1,-1), (2, 1), (2, 0), (2, -1), (2, -2), (1, -2), (0, -2), (-1, -2), (-2, -2)]
        
        allMoves = self.moves["X"] + self.moves["O"]

        for move in allMoves:
            for vector in vectors:
                head = (move[0] + vector[0], move[1] + vector[1])
                tail = (move[0] - vector[0], move[1] - vector[1])
                if not self.isOutOfRange(head) and self.board[head[0]][head[1]] == " ":
                    moveSet.add(head)
                if not self.isOutOfRange(tail) and self.board[tail[0]][tail[1]] == " ":
                    moveSet.add(tail)
        
        return list(moveSet)

    def isOutOfRange(self, pos):
        return pos[0] < 0 or pos[1] < 0 or pos[0] > BOARD_SIZE-1 or pos[1] > BOARD_SIZE-1 
    
# plays the game
def play(game, playerX, playerY):
    game.printBoard()

    letter = "X"
    
    # TODO: or no more available coords
    while game.winner == None:
        print("Player "+letter+" move")
        if letter == "X":
            pos = playerX.makeMove(game)
            game.moves["X"].append(pos)
            game.updateXMoves(pos)
        else:
            pos = playerO.makeMove(game)
            game.moves["O"].append(pos)
            game.updateOMoves(pos)
        
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
    
    
