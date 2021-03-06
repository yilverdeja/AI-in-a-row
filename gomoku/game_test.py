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
    
    # tests if moves are sorted
    def test_makeMove5(self):
        self.testGame.makeMove((1,2), "X")
        self.testGame.makeMove((3,1), "X")
        self.testGame.makeMove((5,6), "X")
        self.testGame.makeMove((4,3), "X")
        self.testGame.makeMove((1,1), "X")
        self.testGame.makeMove((5,4), "X")
        self.assertEqual(self.testGame.moves["X"][0], (1,1))
        self.assertEqual(self.testGame.moves["X"][1], (1,2))
        self.assertEqual(self.testGame.moves["X"][2], (3,1))
        self.assertEqual(self.testGame.moves["X"][3], (4,3))
        self.assertEqual(self.testGame.moves["X"][4], (5,4))
        self.assertEqual(self.testGame.moves["X"][5], (5,6))
    
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
    
    # fills coord 0,0 and determines how many positions are left
    def test_numPositionsLeft(self):
        amount = int(math.pow(game.BOARD_SIZE, 2)) - 1
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertEqual(amount, self.testGame.getNumPosLeft())
    
    # fills coord 0,0 and determines all possible plays 1 square away
    def test_potentialMovesAvailableAtDist1_1(self):
        movesAvailable = 3
        dist = 1
        coord = (0, 0)
        self.testGame.makeMove(coord, "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    # fills coord 0,0 and 0,1 and determines all possible plays 1 square away
    def test_potentialMovesAvailableAtDist1_2(self):
        movesAvailable = 4
        dist = 1
        self.testGame.makeMove((0, 0), "X")
        self.testGame.makeMove((0, 1), "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    # fills coord 0,0; 0,1; and 6,6 and determines all possible plays 1 square away
    def test_potentialMovesAvailableAtDist1_3(self):
        movesAvailable = 12
        dist = 1
        self.testGame.makeMove((0, 0), "X")
        self.testGame.makeMove((0, 1), "X")
        self.testGame.makeMove((6, 6), "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    # fills coord 0,0; 0,1; and 6,6 and determines all possible plays 2 squares away
    def test_potentialMovesAvailableAtDist2_1(self):
        # movesAvailable = 34
        movesAvailable = 25
        dist = 2
        self.testGame.makeMove((0, 0), "X")
        self.testGame.makeMove((0, 1), "X")
        self.testGame.makeMove((6, 6), "X")
        self.assertTrue(len(self.testGame.getPotentialMoves(dist)) == movesAvailable)
    
    # gets direction one square away
    def test_getDirection1(self):
        self.assertEqual(self.testGame.getDirection((0,1),(0,2)), (0, -1))
    
    # gets direction two squares away
    def test_getDirection2(self):
        self.assertEqual(self.testGame.getDirection((0,1),(0,3)), (0, -1))
    
    # gets direction two squares away diagonally in different direction
    def test_getDirection3(self):
        self.assertEqual(self.testGame.getDirection((3,3),(1,1)), (1, 1))
    
    # gets "X"s letter score after a few moves
    def test_getScore1(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((4, 3), "X")
        self.testGame.makeMove((4, 4), "X")
        self.testGame.makeMove((4, 1), "X")
        self.testGame.makeMove((5, 2), "X")
        self.testGame.makeMove((6, 2), "X")
        self.testGame.makeMove((7, 2), "X")
        score = 2 * (game.SCORE_RANK["o3"]) + 5 * (game.SCORE_RANK["o2"]) # 2 * o3 + 5 * o2 = 250
        self.assertEqual(self.testGame.getPlayerScore("X"), score)
    
    # gets "X"s letter score after a few moves
    def test_getScore2(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((4, 3), "X")
        self.testGame.makeMove((4, 4), "X")
        self.testGame.makeMove((4, 1), "X")
        self.testGame.makeMove((5, 2), "X")
        self.testGame.makeMove((6, 2), "X")
        self.testGame.makeMove((6, 3), "X") # new addition
        self.testGame.makeMove((7, 2), "X")
        score = 4 * (game.SCORE_RANK["o3"]) + 5 * (game.SCORE_RANK["o2"]) # 4 * o3 + 5 * o2 = 450
        self.assertEqual(self.testGame.getPlayerScore("X"), score)

    # include "O"s to close off parts
    def test_getScore3(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((4, 3), "X")
        self.testGame.makeMove((4, 4), "X")
        self.testGame.makeMove((4, 1), "X")
        self.testGame.makeMove((5, 2), "X")
        self.testGame.makeMove((6, 2), "X")
        self.testGame.makeMove((7, 2), "X")
        self.testGame.makeMove((4, 2), "O") # new addition to block 4, 2
        score = 1 * (game.SCORE_RANK["c3"]) + 1 * (game.SCORE_RANK["c2"]) + 5 * (game.SCORE_RANK["o2"]) # 1 * c3 + 1 * c2 + 5 * o2
        self.assertEqual(self.testGame.getPlayerScore("X"), score)
    
    # test 4 in a row open
    def test_getScore4(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        scoreX = 1 * (game.SCORE_RANK["o4"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 4 in a row closed
    def test_getScore5(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        self.testGame.makeMove((3, 7), "O")
        scoreX = 1 * (game.SCORE_RANK["c4"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 4 in a row blocked
    def test_getScore6(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        self.testGame.makeMove((3, 2), "O")
        self.testGame.makeMove((3, 7), "O")
        scoreX = 0
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 3 in a row open
    def test_getScore7(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        scoreX = 1 * (game.SCORE_RANK["o3"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 3 in a row closed
    def test_getScore8(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "O")
        scoreX = 1 * (game.SCORE_RANK["c3"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 3 in a row blocked
    def test_getScore9(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 2), "O")
        self.testGame.makeMove((3, 6), "O")
        scoreX = 0
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 2 in a row open
    def test_getScore10(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        scoreX = 1 * (game.SCORE_RANK["o2"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 2 in a row closed
    def test_getScore11(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "O")
        scoreX = 1 * (game.SCORE_RANK["c2"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test 2 in a row blocked
    def test_getScore12(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 2), "O")
        self.testGame.makeMove((3, 5), "O")
        scoreX = 0
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test win condition
    def test_getScore13(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        self.testGame.makeMove((3, 7), "X")
        scoreX = 1 * (game.SCORE_RANK["win"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test win condition
    def test_getScore14(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        self.testGame.makeMove((3, 7), "X")
        self.testGame.makeMove((3, 8), "O")
        scoreX = 1 * (game.SCORE_RANK["win"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test win condition
    def test_getScore15(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        self.testGame.makeMove((3, 7), "X")
        self.testGame.makeMove((3, 8), "O")
        self.testGame.makeMove((3, 2), "O")
        scoreX = 1 * (game.SCORE_RANK["win"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # test win condition and if winner detected
    def test_getScore16(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 6), "X")
        self.assertEqual(self.testGame.winner, None)
        self.testGame.makeMove((3, 7), "X")
        scoreX = 1 * (game.SCORE_RANK["win"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
        self.assertTrue(self.testGame.winner, "X")
    
    # test 4 in a row blocked but gap in middle (should be treated as c4 since it's still possible for a win)
    def test_getScore17(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "X")
        self.testGame.makeMove((3, 5), "X")
        self.testGame.makeMove((3, 7), "X")
        self.testGame.makeMove((3, 2), "O")
        self.testGame.makeMove((3, 8), "O")
        scoreX = 1 * (game.SCORE_RANK["c4"])
        self.assertEqual(self.testGame.getPlayerScore("X"), scoreX)
    
    # X and O scoring is the same as plays go on
    def test_getScoreXO1(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "O")
        self.assertEqual(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        self.testGame.makeMove((4, 3), "X")
        self.testGame.makeMove((4, 4), "O")
        self.assertEqual(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        self.testGame.makeMove((5, 3), "X")
        self.testGame.makeMove((5, 4), "O")
        self.assertEqual(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        self.testGame.makeMove((6, 3), "X")
        self.testGame.makeMove((6, 4), "O")
        self.assertEqual(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        self.testGame.makeMove((7, 3), "X")
        self.testGame.makeMove((7, 4), "O")
        self.assertEqual(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
    
    def test_getScoreXO2(self):
        self.testGame.makeMove((3, 3), "X")
        self.testGame.makeMove((3, 4), "O")
        self.testGame.makeMove((4, 3), "X")
        self.testGame.makeMove((5, 3), "O")
        self.assertGreater(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        self.testGame.makeMove((2, 3), "X")
        self.testGame.makeMove((4, 4), "O")
        self.testGame.makeMove((4, 2), "X")
        self.testGame.makeMove((5, 4), "O")
        self.assertLess(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))
        self.testGame.makeMove((2, 4), "X")
        self.testGame.makeMove((5, 1), "O")
        self.assertLess(self.testGame.getPlayerScore("X"), self.testGame.getPlayerScore("O"))

if __name__ == "__main__":
    unittest.main()