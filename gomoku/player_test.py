import unittest
import game
import math
from player import AIPlayer

class TestGame(unittest.TestCase):

    def setUp(self):
        self.testGame = game.Game()
        # self.playerAI = AIPlayer("X")
        # board setup
    
    def test_playerMove1(self):
        self.playerAI = AIPlayer("X")
        self.testGame.makeMove((6, 6), "X")
        self.testGame.makeMove((7, 6), "X")
        self.testGame.makeMove((7, 7), "X")
        self.testGame.makeMove((8, 6), "X")
        self.testGame.makeMove((6, 8), "O")
        self.testGame.makeMove((7, 8), "O")
        self.testGame.makeMove((8, 7), "O")
        self.testGame.makeMove((9, 6), "O")
        # print(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        coord = self.playerAI.makeMove(self.testGame)
        possiblePlay1 = (6,9)
        possiblePlay2 = (10,5)
        # print(coord)
        self.assertTrue(coord == possiblePlay1 or coord == possiblePlay2)
    
    def test_playerMove2(self):
        self.playerAI = AIPlayer("X")
        self.testGame.makeMove((6, 10), "X")
        self.testGame.makeMove((7, 9), "X")
        self.testGame.makeMove((8, 8), "X")
        self.testGame.makeMove((9, 7), "X")
        self.testGame.makeMove((1, 1), "O")
        self.testGame.makeMove((8, 9), "O")
        self.testGame.makeMove((8, 10), "O")
        self.testGame.makeMove((9, 5), "O")
        print(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        coord = self.playerAI.makeMove(self.testGame)
        possiblePlay1 = (5,11)
        possiblePlay2 = (10,6)
        print(coord)
        self.assertTrue(coord == possiblePlay1 or coord == possiblePlay2)
    
    # test doesn't work as expected... plays on (14, 10)
    def test_playerMove3(self):
        self.playerAI = AIPlayer("O")
        self.testGame.makeMove((5, 9), "X")
        self.testGame.makeMove((6, 7), "X")
        self.testGame.makeMove((6, 11), "X")
        self.testGame.makeMove((7, 8), "X")
        self.testGame.makeMove((7, 9), "X")
        self.testGame.makeMove((8, 6), "X")
        self.testGame.makeMove((8, 8), "X")
        self.testGame.makeMove((8, 10), "X")
        self.testGame.makeMove((9, 6), "X")
        self.testGame.makeMove((9, 7), "X")
        self.testGame.makeMove((9, 8), "X")
        self.testGame.makeMove((9, 10), "X")
        self.testGame.makeMove((12, 6), "X")
        
        self.testGame.makeMove((6, 8), "O")
        self.testGame.makeMove((6, 9), "O")
        self.testGame.makeMove((6, 10), "O")
        self.testGame.makeMove((7, 7), "O")
        self.testGame.makeMove((7, 10), "O")
        self.testGame.makeMove((8, 9), "O")
        self.testGame.makeMove((9, 5), "O")
        self.testGame.makeMove((9, 7), "O")
        self.testGame.makeMove((10, 6), "O")
        self.testGame.makeMove((10, 8), "O")
        self.testGame.makeMove((11, 7), "O")
        self.testGame.makeMove((12, 8), "O")
        print(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        coord = self.playerAI.makeMove(self.testGame)
        possiblePlay1 = (8,4)
        possiblePlay2 = (13,9)
        print(coord)
        self.assertTrue(coord == possiblePlay1 or coord == possiblePlay2)

if __name__ == "__main__":
    unittest.main()
        