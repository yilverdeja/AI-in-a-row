import unittest
import game
import math
from player import AIPlayer

class TestGame(unittest.TestCase):

    def setUp(self):
        self.testGame = game.Game()
        self.playerAI = AIPlayer("X")
        # board setup
    
    def test_playerMove1(self):
        self.testGame.makeMove((6, 6), "X")
        self.testGame.makeMove((7, 6), "X")
        self.testGame.makeMove((7, 7), "X")
        self.testGame.makeMove((8, 6), "X")
        self.testGame.makeMove((6, 8), "O")
        self.testGame.makeMove((7, 8), "O")
        self.testGame.makeMove((8, 7), "O")
        self.testGame.makeMove((9, 6), "O")
        print(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        coord = self.playerAI.makeMove(self.testGame)
        possiblePlay1 = (6,9)
        possiblePlay2 = (10,5)
        print(coord)
        self.assertTrue(coord == possiblePlay1 or coord == possiblePlay2)

if __name__ == "__main__":
    unittest.main()
        