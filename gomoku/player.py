import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def makeMove(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        while True:
            rowPos = self.getPosition("row")
            colPos = self.getPosition("col")

            if game.makeMove((rowPos, colPos), self.letter):
                break
            else:
                print("Must choose an empty position on the board!")

        return

    def getPosition(self, posType):
        while True:
            pos = int(input(posType+" (0-14): "))
            if pos >= 0 and pos <= 14:
                return pos
            else:
                print("Must choose a position between 0 and 14")

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        return
    
    # minimax algorithm with alpha beta pruning
    def minimax(self):
        return
    
    # heuristics that evaluate which move is the best
    def heuristics(self):
        # look at gomoku strategies
        return