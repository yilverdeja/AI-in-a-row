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
        return

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