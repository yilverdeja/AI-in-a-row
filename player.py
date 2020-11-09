import random
import math
# can choose type of player (human, random, AI)

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def makeMove(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        coords = game.getAvailableCoords()
        while True:
            moveCoord = int(input("pos: "))
            if (moveCoord in coords):
                break
        game.makeMove(moveCoord, self.letter)

class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        coords = game.getAvailableCoords()
        moveCoord = random.choice(coords)
        game.makeMove(moveCoord, self.letter)

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        # minimax + alpha beta pruning
        return