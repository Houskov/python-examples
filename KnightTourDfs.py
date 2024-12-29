#kun po sachovnici

class ChessBoardMoves:
    
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
            print(self.board)
            self.solutionFound = True
            return
        elif not self.solutionFound:
            for i in range(len(self.knightMoves)):
                newx = currentX + self.knightMoves[i][0]
                newy = currentY + self.knightMoves[i][1]
                if newx in range(self.columns) and newy in range(self.rows) and self.board[newx][newy] == -1:
                    self.board[newx][newy] = depth + 1
                    self.dfsKnightTour(newx, newy)
                    if not self.solutionFound:
                        self.board[newx][newy] = -1
    def printBoard(self):
        print(self.board)

movements = ChessBoardMoves(0,4)
movements.knightTour()