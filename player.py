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
        # minimizingPlayer = "X" if self.letter == "O" else "X"
        print("AI Move")

        if game.isBoardEmpty():
            # place in the corners
            moveCoord = random.choice(game.getCornerCoords())
        else:
            # minimax
            # moveCoord = (self.minimax(game, len(game.getAvailableCoords()), True))[1]
            print("moveCoord: ",moveCoord)

        game.makeMove(moveCoord, self.letter)
    
    def minimax(self, gameState, depth, isMaxPlayer):
        return 1


    def minimax1(self, gameState, depth, isMaxPlayer):
        # print("minimax, depth:", depth)
        maxPlayer = self.letter
        minPlayer = "X" if maxPlayer == "O" else "O"

        if depth == 0:
            # return evaluation, -1 if minPlayer wins, +1 if maxPlayer wins, and 0 if no wins
            if gameState.winner == maxPlayer:
                return [1, -1]
            elif gameState.winner == minPlayer:
                return [-1, -1]
            else:
                return [0, -1]
        
        if isMaxPlayer:
            maxEval = -1<<31
            maxChild = -1
            for child in gameState.getAvailableCoords():
                # play the state and check minimax algo
                gameState.makeMove(child, maxPlayer)
                eval = (self.minimax1(gameState, depth-1, False))[0]
                # print("eval: ",eval)
                gameState.undoMove(child, maxPlayer)
                print("maxEval: ",maxEval,"eval: ",eval)
                if eval > maxEval:
                    print("updateVals")
                    maxChild = child
                maxEval = max(maxEval, eval)
            # print("max: ", maxEval, maxChild)
            return [maxEval, maxChild]
        else:
            minEval = 1<<31
            minChild = -2
            for child in gameState.getAvailableCoords():
                # play the state and check minimax algo
                gameState.makeMove(child, minPlayer)
                eval = (self.minimax1(gameState, depth-1, True))[0]
                # print("eval: ",eval)
                gameState.undoMove(child, minPlayer)
                if eval < minEval:
                    minChild = child
                minEval = min(minEval, eval)
            # print("min: ", minEval, minChild)
            return [minEval, minChild]
        
