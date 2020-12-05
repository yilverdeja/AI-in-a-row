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
                return (rowPos, colPos)
            else:
                print("Must choose an empty position on the board!")

    def getPosition(self, posType):
        while True:
            pos = int(input(posType+" (1-3): "))
            if pos >= 1 and pos <= 3:
                return pos-1
            else:
                print("Must choose a position between 1 and 3")

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        if game.isBoardEmpty():
            # place randomly
            pos = random.choice(game.getPotentialMoves())
            if game.makeMove(pos, self.letter):
                return pos
            else:
                raise Exception("Something is wrong. You should be able to make a move if the board is empty...")
        else:
            # minimax
            depth = 5
            eval = self.minimax(game, depth, -math.inf, math.inf, True)
            if game.makeMove(eval["position"], self.letter):
                return eval["position"]
            else:
                raise Exception("Something wrong with minimax output. It should be able to play the move.")
            
        return
    
    # minimax algorithm with alpha beta pruning
    def minimax(self, gameState, depth, alpha, beta, isMaximizing):
        maxPlayer = self.letter
        minPlayer = "X" if maxPlayer == "O" else "O"

        if depth == 0 or gameState.winner != None:
            if gameState.winner == maxPlayer:
                return {"score": 1*(gameState.getNumMovesLeft() + 1), "position": None}
            elif gameState.winner == minPlayer:
                return {"score": -1*(gameState.getNumMovesLeft() + 1), "position": None}
            else:
                return {"score": 0, "position": None}

        elif gameState.isBoardFull():
            # A tie
            return {"score": 0, "position": None}
        
        if isMaximizing:
            bestPlay = {"score": -math.inf, "position": None}
            player = maxPlayer
        else:
            bestPlay = {"score": math.inf, "position": None}
            player = minPlayer

        for posChild in gameState.getPotentialMoves():
            gameState.makeMove(posChild, player)
            eval = self.minimax(gameState, depth-1, alpha, beta, not isMaximizing)

            gameState.undoMove(posChild, player)
            eval['position'] = posChild

            if isMaximizing:
                if eval["score"] > bestPlay["score"]:
                    bestPlay = eval
                alpha = max(alpha, eval["score"])
                if beta <= alpha:
                    break
            else:
                if eval["score"] < bestPlay["score"]:
                    bestPlay = eval
                beta = min(beta, eval["score"])
                if beta <= alpha:
                    break

        return bestPlay