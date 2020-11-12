import random
import math

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
        return moveCoord

class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        coords = game.getAvailableCoords()
        moveCoord = random.choice(coords)
        game.makeMove(moveCoord, self.letter)
        return moveCoord

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def makeMove(self, game):
        # minimax + alpha beta pruning
        print("AI Moves")

        if game.isBoardEmpty():
            # place in the corners
            # moveCoord = random.choice(game.getCornerCoords())
            coords = game.getAvailableCoords()
            moveCoord = random.choice(coords)
        else:
            # minimax
            depth = len(game.getAvailableCoordsInProximity())
            score = (self.minimax(game, depth, -math.inf, math.inf, True))
            # print("score: ", score)
            moveCoord = score["position"]
            # print("moveCoord: ",moveCoord)

        game.makeMove(moveCoord, self.letter)
        return moveCoord


    def minimax(self, gameState, depth, alpha, beta, isMaxPlayer):
        maxPlayer = self.letter
        minPlayer = "X" if maxPlayer == "O" else "O"

        if depth == 0 or gameState.winner != None:
            # return evaluation, -1 if minPlayer wins, +1 if maxPlayer wins, and 0 if no wins
            if gameState.winner == maxPlayer:
                return {"score": 1 * (len(gameState.getAvailableCoords()) + 1), "position": None}
            elif gameState.winner == minPlayer:
                return {"score": -1 * (len(gameState.getAvailableCoords()) + 1), "position": None}
            else:
                return {"score": 0, "position": None}
        
        if isMaxPlayer:
            bestScore = {"score": -math.inf, "position": None}
            player = maxPlayer
        else:
            bestScore = {"score": math.inf, "position": None}
            player = minPlayer
        
        for posChild in gameState.getAvailableCoordsInProximity():
            gameState.makeMove(posChild, player)
            eval = self.minimax(gameState, depth-1, alpha, beta, not isMaxPlayer)

            gameState.undoMove(posChild, player)
            eval['position'] = posChild

            if isMaxPlayer:
                if eval["score"] > bestScore["score"]:
                    bestScore = eval
                alpha = max(alpha, eval["score"])
                if beta <= alpha:
                    break
            else:
                if eval["score"] < bestScore["score"]:
                    bestScore = eval
                beta = min(beta, eval["score"])
                if beta <= alpha:
                    break

        return bestScore 
        
