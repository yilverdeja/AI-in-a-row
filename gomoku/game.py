import math
import operator
from player import HumanPlayer, AIPlayer

# TODO: don't hardcode in player.py
BOARD_SIZE = 15

class Game():

    def __init__(self):
        self.board = self.makeBoard()
        self.moves = {"X": [], "O": []}
        self.winner = None
    
    # Makes the 15x15 board to play Gomoku
    @staticmethod
    def makeBoard():
        return [[" " for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
    # prints a 15x15 board
    def printBoard(self):
        for i in range(BOARD_SIZE):
            print('| ' + ' | '.join(self.board[i]) + ' |')
                
    # Attempts to make a move on the board
    def makeMove(self, coord, letter):
        self.__checkIfValidLetter(letter)

        if self.isOutOfRange(coord): return False
        if (self.board[coord[0]][coord[1]] == " "):
            self.board[coord[0]][coord[1]] = letter
            self.moves[letter].append(coord)
            self.__sortMoves(letter)
            # TODO: check winner?
            return True
        return False
    
    # Attempts to undo a move on the board
    def undoMove(self, coord, letter):
        self.__checkIfValidLetter(letter)

        if self.isOutOfRange(coord): return False
        if (self.board[coord[0]][coord[1]] == letter):
            self.moves[letter].remove(coord)
            # self.__sortMoves(letter) # should already be sorted
            self.board[coord[0]][coord[1]] = " "
            if self.winner != None:
                self.winner = None
            return True
        return False
    
    def __checkIfValidLetter(self, letter):
        if letter != "X" and letter != "O":
            raise Exception("Input letter must either be X or O!")

    def __sortMoves(self, letter):
        self.__checkIfValidLetter(letter)
        self.moves[letter].sort(key = lambda x: (x[0], x[1]))
    
    # checks if board is empty
    def isBoardEmpty(self):
        return len(self.moves["X"]) == 0 and len(self.moves["O"]) == 0
    
    # checks if the board is full
    def isBoardFull(self):
        return len(self.moves["X"]) + len(self.moves["O"]) >= int(math.pow(BOARD_SIZE, 2))
    
    # gets the number of positions left on the board
    def getNumPosLeft(self):
        return int(math.pow(BOARD_SIZE, 2)) - len(self.moves["X"]) - len(self.moves["O"])
    
    # gets the player score on that current board
    def getPlayerScore(self, letter):
        self.__checkIfValidLetter(letter)

        # c2, o2, c3, o3, c4, o4
        # scoreRank = [5, 10, 25, 100, 1000, 10000]
        scoreRank = {"c2": 5, "o2": 10, "c3": 25, "o3": 100, "c4": 1000, "o4": 10000}
        typeRank = {"c2": 0, "o2": 0, "c3": 0, "o3": 0, "c4": 0, "o4": 0}

        # totalScore
        totalScore = 0

        checkedMoves = []
        playerMoves = self.moves[letter].copy()
        if letter == "X":
            enemyMoves = self.moves["O"].copy()
        else:
            enemyMoves = self.moves["X"].copy()

        # pops the first value from completed moves and checks if it has any neighbors within completed moves. Once a neighbor is found, and looks further in it's direction. Once that's complete, it gets the length of the move and adds it to the score. Then it keeps going through neighbors until all of them have been visited. Once complete, adds that move into checkedMoves and then pops the next item inside playerMoves. Repeats until playerMoves has a length of 0

        while len(playerMoves) > 0:
            checkMove = playerMoves.pop(0)
            print("checkmove", checkMove)
            neighborMoves = self.getNeighbors(checkMove)
            checkedNeighbors = set()
            # print(checkMove, neighborMoves)
            for neighbor in neighborMoves:
                
                # print(neighbor in playerMoves)
                # print(checkMove, neighbor, playerMoves)
                if neighbor in checkedNeighbors:
                    continue

                if neighbor in playerMoves:
                    direction = self.getDirection(checkMove, neighbor)
                    neighborCount = 1
                    moveType = "o" # or "c" or maybe "b" for blocked

                    # head
                    aPos = tuple(map(operator.add, checkMove, direction))
                    bPos = tuple(map(operator.add, aPos, direction))
                    # print("head", aPos, bPos)

                    foundFlag = aPos in checkedMoves or bPos in checkedMoves
                    if foundFlag:
                        print("flag found", checkMove, aPos, bPos)
                        continue

                    while aPos in playerMoves or bPos in playerMoves:
                        checkedNeighbors.update([aPos, bPos])
                        if aPos in playerMoves and bPos in playerMoves:
                            # print("inc 2 head", checkMove, aPos, bPos)
                            neighborCount = neighborCount + 2
                        elif aPos in enemyMoves:
                            moveType = "c"
                            # print("escape")
                            break
                        else:
                            neighborCount = neighborCount + 1
                            # print("inc 1 head", checkMove, aPos, bPos)
                            if bPos in enemyMoves:
                                moveType = "c"
                                # print("escape")
                                break
            
                        aPos = tuple(map(operator.add, bPos, direction))
                        bPos = tuple(map(operator.add, aPos, direction))
                    
                    # print("after head")
                    
                    # tail
                    aPos = tuple(map(operator.sub, checkMove, direction))
                    bPos = tuple(map(operator.sub, aPos, direction))

                    foundFlag = aPos in checkedMoves or bPos in checkedMoves
                    if foundFlag:
                        # print("flag found", checkMove, aPos, bPos)
                        continue

                    while aPos in playerMoves or bPos in playerMoves:
                        checkedNeighbors.update([aPos, bPos])
                        if aPos in playerMoves and bPos in playerMoves:
                            # print("inc 2 tail", checkMove, aPos, bPos)
                            neighborCount = neighborCount + 2
                        elif aPos in enemyMoves:
                            moveType = "c"
                            # print("escape")
                            break
                        else:
                            neighborCount = neighborCount + 1
                            # print("inc 1 tail", checkMove, aPos, bPos)
                            if bPos in enemyMoves:
                                moveType = "c"
                                # print("escape")
                                break

                        aPos = tuple(map(operator.sub, bPos, direction))
                        bPos = tuple(map(operator.sub, aPos, direction))
                    
                    # print("after tail")

                    tRank = moveType + str(neighborCount)
                    print(tRank)
                    typeRank[tRank] = typeRank[tRank] + 1
                    checkedNeighbors.add(neighbor)
            
            checkedMoves.append(checkMove)
        print(typeRank)

        for key in scoreRank:
            score = scoreRank[key] * typeRank[key]
            totalScore = totalScore + score
            
        return totalScore

    # gets neighbors a distance of 2 from the coord
    def getNeighbors(self, coord):
        moveSet = set()
        # vectors = [(-1, 0), (0, -1), (-1,-1), (1,-1), (2, 1), (2, 0), (2, -1), (2, -2), (1, -2), (0, -2), (-1, -2), (-2, -2)]
        vectors = [(-1, 0), (0, -1), (-1,-1), (1,-1), (2, 0), (2, -2), (0, -2), (-2, -2)]
        for vector in vectors:
            head = (coord[0] + vector[0], coord[1] + vector[1])
            tail = (coord[0] - vector[0], coord[1] - vector[1])
            if not self.isOutOfRange(head):
                moveSet.add(head)
            if not self.isOutOfRange(tail):
                moveSet.add(tail)
        
        return list(moveSet)

    
    # def getPlayerScore(self, letter):
    #     # TODO is there a better way to simplify this
    #     if letter == "X":
    #         return 1000*len(xMoves["4"]) + 100*len(xMoves["c4"]) + 50*len(xMoves["3"]) + 25*len(xMoves["c3"]) + 10*len(xMoves["2"]) + 5*len(xMoves["c2"])
    #     elif letter == "O":
    #         return 1000*len(oMoves["4"]) + 100*len(oMoves["c4"]) + 50*len(oMoves["3"]) + 25*len(oMoves["c3"]) + 10*len(oMoves["2"]) + 5*len(oMoves["c2"])

    def getDirection(self, t1, t2):
        # https://www.geeksforgeeks.org/python-how-to-get-subtraction-of-tuples/
        direction = tuple(map(operator.sub, t1, t2))
        if direction[0] != 0 or abs(direction[0]) == abs(direction[1]):
            direction = tuple(int(i/abs(direction[0])) for i in direction)
        elif direction[1] != 0:
            direction = tuple(int(i/abs(direction[1])) for i in direction)
        return direction

    # TODO refactor with get neighbors if possible
    def getPotentialMoves(self, dist):
        moveSet = set()
        if dist == 1:
            vectors = [(1, 0), (0, 1), (1,1), (1,-1)]
        elif dist == 2:
            # vectors = [(-1, 0), (0, -1), (-1,-1), (1,-1), (2, 1), (2, 0), (2, -1), (2, -2), (1, -2), (0, -2), (-1, -2), (-2, -2)]
            # should only play what's in line to each coord
            vectors = [(-1, 0), (0, -1), (-1,-1), (1,-1), (2, 0), (2, -2), (0, -2), (-2, -2)]
        else:
            raise Exception("Dist must be either 1 or 2!")
        
        allMoves = self.moves["X"] + self.moves["O"]

        for move in allMoves:
            for vector in vectors:
                head = (move[0] + vector[0], move[1] + vector[1])
                tail = (move[0] - vector[0], move[1] - vector[1])
                if not self.isOutOfRange(head) and self.board[head[0]][head[1]] == " ":
                    moveSet.add(head)
                if not self.isOutOfRange(tail) and self.board[tail[0]][tail[1]] == " ":
                    moveSet.add(tail)
        
        return list(moveSet)

    def isOutOfRange(self, pos):
        return pos[0] < 0 or pos[1] < 0 or pos[0] > BOARD_SIZE-1 or pos[1] > BOARD_SIZE-1 
    
# plays the game
def play(game, playerX, playerY):
    game.printBoard()

    letter = "X"
    
    # TODO: or no more available coords
    while game.winner == None:
        print("Player "+letter+" move")
        if letter == "X":
            pos = playerX.makeMove(game)
            game.moves["X"].append(pos)
        else:
            pos = playerO.makeMove(game)
            game.moves["O"].append(pos)
        
        game.printBoard()
        print(game.moves)

        # swap player
        letter = "X" if letter == "O" else "O"

    return

if __name__ == "__main__":
    g = Game()
    playerX = AIPlayer("X")
    playerO = HumanPlayer("O")
    play(g, playerX, playerO)
    
    
