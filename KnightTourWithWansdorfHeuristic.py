#kun po sachovnici

class ChessBoardMoves:
    class MoveWithPriority:
        def __init__(self, x, y, nextMoves):
            self.x = x
            self.y = y
            self.nextMoves = nextMoves
    
    def __init__(self, startX, startY):
        self.knightMoves = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
        self.board = []
        self.columns = 8
        self.rows = 8
        self.startX = startX
        self.startY = startY
        self.solutionFound = False
        self.initBoard()

    def initBoard(self):
        for i in range (self.columns):
            collumn = []
            for j in range (self.rows):
                collumn.append(-1)
            self.board.append(collumn)

    def knightTour(self):
        self.board[self.startX][self.startY] = 1
        self.solutionFound = False
        self.dfsKnightTour(self.startX, self.startY)


    def dfsKnightTour(self,currentX, currentY):
        depth = self.board[currentX][currentY]
        if depth == 64:
            self.printBoard()
            self.solutionFound = True
            return
        elif not self.solutionFound:
            movesByPriority = self.getMovesSortedByFewestNextPossibleMoves(currentX, currentY)
            if movesByPriority != None:
                for i in range(len(movesByPriority)):
                    nextMove = movesByPriority[i]
                    self.board[nextMove.x][nextMove.y] = depth + 1
                    self.dfsKnightTour(nextMove.x, nextMove.y)
                    if not self.solutionFound:
                        self.board[nextMove.x][nextMove.y] = -1

    def getMovesSortedByFewestNextPossibleMoves(self, x, y):
        movesByPriority = []
        for i in range(len(self.knightMoves)):
            newx = x + self.knightMoves[i][0]
            newy = y + self.knightMoves[i][1]
            possibleMoves = 0
            if newx in range(self.columns) and newy in range(self.rows) and self.board[newx][newy] == -1:
                for j in range(len(self.knightMoves)):
                    nextX = newx + self.knightMoves[j][0]
                    nextY = newy + self.knightMoves[j][1]
                    if nextX in range(self.columns) and nextY in range(self.rows) and self.board[nextX][nextY] == -1:    
                        possibleMoves += 1
                movesByPriority.append(self.MoveWithPriority(newx, newy, possibleMoves))
        movesByPriority.sort(key=lambda p: p.nextMoves)
        return movesByPriority

    def printBoard(self):
        print(self.board)


movements = ChessBoardMoves(4,4)
movements.knightTour()