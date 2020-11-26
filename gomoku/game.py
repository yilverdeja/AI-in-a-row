import math
import operator
from player import HumanPlayer, AIPlayer

# TODO: don't hardcode in player.py
BOARD_SIZE = 15
SCORE_RANK = {"c2": 5, "o2": 10, "c3": 25, "o3": 100, "c4": 1000, "o4": 10000, "win": 100000}
MOVES_TO_WIN = 5

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
    
    # private function to check if the letter is either X or O
    def __checkIfValidLetter(self, letter):
        if letter != "X" and letter != "O":
            raise Exception("Input letter must either be X or O!")

    # private function to sort the moves played on the board when a move is made
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
        
        # typeRank = {"c2": 0, "o2": 0, "c3": 0, "o3": 0, "c4": 0, "o4": 0}
        typeRank = {"c2": 0, "o2": 0, "c3": 0, "o3": 0, "c4": 0, "o4": 0, "win": 0}

        # totalScore
        totalScore = 0

        # determines the moves that have already been checked
        # will be used to cross check neighboring moves
        checkedMoves = []

        # getting all player moves and enemy moves
        playerMoves = self.moves[letter].copy()
        if letter == "X":
            enemyMoves = self.moves["O"].copy()
        else:
            enemyMoves = self.moves["X"].copy()

        while len(playerMoves) > 0:
            move = playerMoves.pop(0)
            neighbors = self.getNeighbors(move)
            checkedNeighbors = set()

            for neighbor in neighbors:
                if neighbor in checkedNeighbors:
                    continue

                if neighbor in playerMoves:
                    direction = self.getDirection(move, neighbor)

                    lenCount = 1
                    headBlock = False
                    tailBlock = False
                    flag = False

                    print(move, neighbor, direction)
                    
                    # head search
                    head = tuple(map(operator.add, move, direction))
                    headBreak = False

                    if head in checkedMoves:
                        flag = True

                    if self.isOutOfRange(head) or head in enemyMoves:
                        headBlock = True
                    elif head not in playerMoves and not headBreak:
                        headBreak = True
                        head = tuple(map(operator.add, head, direction))
                        if head in checkedMoves:
                            flag = True

                    while head in playerMoves and not flag:
                        print("head: ", head)
                        lenCount+=1
                        checkedNeighbors.add(head)
                        head = tuple(map(operator.add, head, direction))
                        if head in checkedMoves:
                            flag = True
                            break
                        if self.isOutOfRange(head) or head in enemyMoves:
                            headBlock = True
                            break
                        if head not in playerMoves and not headBreak:
                            headBreak = True
                            head = tuple(map(operator.add, head, direction))
                            if head in checkedMoves:
                                flag = True
                                break
                    
                    # tail search
                    tail = tuple(map(operator.sub, move, direction))
                    tailBreak = False

                    if tail in checkedMoves:
                        flag = True

                    if self.isOutOfRange(tail) or tail in enemyMoves:
                        print("tail oor or enemy")
                        tailBlock = True
                    elif tail not in playerMoves and not tailBreak:
                        print("tail not in pm", tail)
                        tailBreak = True
                        tail = tuple(map(operator.sub, tail, direction))
                        print("new tail", tail)
                        if tail in checkedMoves:
                            flag = True

                    while tail in playerMoves and not flag:
                        print("tail: ", tail)
                        lenCount+=1
                        checkedNeighbors.add(tail)
                        tail = tuple(map(operator.sub, tail, direction))
                        if tail in checkedMoves:
                            flag = True
                            break
                        if self.isOutOfRange(tail) or tail in enemyMoves:
                            tailBlock = True
                            break
                        if tail not in playerMoves and not tailBreak:
                            tailBreak = True
                            tail = tuple(map(operator.sub, tail, direction))
                            if tail in checkedMoves:
                                flag = True
                                break
                    
                    if flag:
                        continue

                    print("lenCount: ", lenCount)
                    
                    # add to ranks
                    if not tailBlock and not headBlock:
                        moveType = "o"
                    elif (not tailBlock and headBlock) or (tailBlock and not headBlock):
                        moveType = "c"
                    else:
                        moveType = "b"

                    print("moveType", moveType)

                    if (lenCount < 5 and lenCount > 1) and moveType != "b":
                        tRank = moveType + str(lenCount)
                        typeRank[tRank] += 1
                    elif lenCount == 4 and moveType == "b" and (tailBreak or headBreak):
                        typeRank["c4"] += 1
                    elif lenCount >= 5:
                        typeRank["win"] += 1

                    checkedNeighbors.add(neighbor)
            
            checkedMoves.append(move)
        
        print(typeRank)

        for key in SCORE_RANK:
            score = SCORE_RANK[key] * typeRank[key]
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
    
    
