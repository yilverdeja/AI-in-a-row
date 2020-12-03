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
            pos = int(input(posType+" (0-14): "))
            if pos >= 0 and pos <= 14:
                return pos
            else:
                print("Must choose a position between 0 and 14")

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        if game.isBoardEmpty():
            # place randomly in center
            pos = random.choice([(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)])
            if game.makeMove(pos, self.letter):
                return pos
            else:
                raise Exception("Something is wrong. You should be able to make a move if the board is empty...")
        else:
            # minimax
            depth = 2
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

        if gameState.winner != None:
            if gameState.winner == maxPlayer:
                return {"score": 1*(gameState.getNumPosLeft() + 1)*(gameState.getPlayerScore(maxPlayer)), "position": None}
            elif gameState.winner == minPlayer:
                return {"score": -1*(gameState.getNumPosLeft() + 1)*(gameState.getPlayerScore(minPlayer)), "position": None}
        elif depth == 0:
            # Get combinations that each player has on board
            maxPlayerScore = 1*gameState.getPlayerScore(maxPlayer)
            minPlayerScore = -1*gameState.getPlayerScore(minPlayer)
            score = minPlayerScore + maxPlayerScore
            return {"score": score, "position": None}
            
        elif gameState.isBoardFull():
            # A tie
            return {"score": 0, "position": None}
        
        # TODO rest of minimax
        if isMaximizing:
            bestPlay = {"score": -math.inf, "position": None}
            player = maxPlayer
        else:
            bestPlay = {"score": math.inf, "position": None}
            player = minPlayer

        # TODO iterate through every open pos that's a dist of 2 away
        for posChild in gameState.getPotentialMoves(2):
            gameState.makeMove(posChild, player)
            eval = self.minimax(gameState, depth-1, alpha, beta, not isMaximizing)
            # print("eval, ", eval)

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