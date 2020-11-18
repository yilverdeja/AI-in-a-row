import unittest
import game
import math

class TestGame(unittest.TestCase):

    def setUp(self):
        self.testGame = game.Game()
    
    # attempts to make a valid move at an empty coord
    def test_makeMove1(self):
        coord = (0, 0)
        self.assertTrue(self.testGame.makeMove(coord, "X"))

    # makes a move and checks if move was made at the correct coord
    def test_makeMove2(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        testLetter = (self.testGame.board)[0][0]
        self.assertTrue(testLetter == "X" and self.testGame.moves["X"][0] == coord)
    
    # tries to make move on top of a played coord
    def test_makeMove3(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertFalse(self.testGame.makeMove(coord, "O"))
    
    # makes 4 invalid moves
    def test_makeMove4(self):
        invalidMove1 = self.testGame.makeMove((-1, 0), "X")
        invalidMove2 = self.testGame.makeMove((0, -1), "X")
        invalidMove3 = self.testGame.makeMove((game.BOARD_SIZE, 0), "X")
        invalidMove4 = self.testGame.makeMove((0, game.BOARD_SIZE), "X")
        self.assertFalse(invalidMove1 or invalidMove2 or invalidMove3 or invalidMove4)
    
    # undoes "X" at coord 0, 0 after it's played there
    def test_undoMove1(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertTrue(self.testGame.undoMove(coord, "X"))
    
    # cannot undo a move that's not the same letter
    def test_undoMove2(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertFalse(self.testGame.undoMove(coord, "O"))
    
    # makes 4 invalid undo moves
    def test_undoMove3(self):
        invalidMove1 = self.testGame.undoMove((-1, 0), "X")
        invalidMove2 = self.testGame.undoMove((0, -1), "X")
        invalidMove3 = self.testGame.undoMove((game.BOARD_SIZE, 0), "X")
        invalidMove4 = self.testGame.undoMove((0, game.BOARD_SIZE), "X")
        self.assertFalse(invalidMove1 or invalidMove2 or invalidMove3 or invalidMove4)
    
    # leaves the board empty
    def test_emptyBoard1(self):
        self.assertTrue(self.testGame.isBoardEmpty())
    
    # fills only coord 0, 0
    def test_emptyBoard2(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertFalse(self.testGame.isBoardEmpty())
    
    # makes a move and undoes it
    def test_emptyBoard3(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.testGame.undoMove(coord, "X")
        self.assertTrue(self.testGame.isBoardEmpty())
    
    # leaves the board empty
    def test_fullBoard1(self):
        self.assertFalse(self.testGame.isBoardFull())
    
    # fills only coord 0, 0
    def test_fullBoard2(self):
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertFalse(self.testGame.isBoardFull())
    
    # fills the whole board
    def test_fullBoard3(self):
        for i in range(game.BOARD_SIZE):
            for j in range(game.BOARD_SIZE):
                self.testGame.makeMove((i, j), "X")
        self.assertTrue(self.testGame.isBoardFull())
    
    # fills the board but leaves (0, 0) empty
    def test_fullBoard4(self):
        for i in range(game.BOARD_SIZE):
            for j in range(game.BOARD_SIZE):
                self.testGame.makeMove((i, j), "X")
        self.testGame.undoMove((0, 0), "X")
        self.assertFalse(self.testGame.isBoardFull())
    
    def test_numPositionsLeft(self):
        amount = int(math.pow(game.BOARD_SIZE, 2)) - 1
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertEqual(amount, self.testGame.getNumPosLeft())
    
    def test_potentialMovesAvailableAtDist1(self):
        movesAvailable = 3
        dist = 1
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    def test_potentialMovesAvailableAtDist2(self):
        movesAvailable = 4
        dist = 1
        self.testGame.makeMove((0, 0), "X")
        self.testGame.makeMove((0, 1), "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    def test_potentialMovesAvailableAtDist3(self):
        movesAvailable = 12
        dist = 1
        self.testGame.makeMove((0, 0), "X")
        self.testGame.makeMove((0, 1), "X")
        self.testGame.makeMove((6, 6), "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    # test get direction




if __name__ == "__main__":
    unittest.main()