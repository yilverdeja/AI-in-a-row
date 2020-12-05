import unittest
import game
import math

class TestGame(unittest.TestCase):

    def setUp(self):
        self.testGame = game.Game()
    
    # attempts to make a valid move at an empty coord
    def test_makeMove1(self):
        coord = (0, 0)
        self.assertTrue(self.testGame.makeMove(coord, "X")) # layer 1 - valid
        self.assertTrue(self.testGame.makeMove(coord, "X")) # layer 2 - valid
        self.assertTrue(self.testGame.makeMove(coord, "X")) # layer 3 - valid
        self.assertFalse(self.testGame.makeMove(coord, "X")) # layer "4" - invalid

if __name__ == "__main__":
    unittest.main()