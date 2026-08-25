class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def dfs(placed):
            if len(placed) == n:
                # completed 
                board = []
                for col in placed:
                    template = "."*col + "Q" + "."*(n-col-1)
                    board.append(template)
                solutions.append(board)
                return
            currRow = len(placed)
            for currCol in range(n):
                isValid = True
                for row, col in enumerate(placed):
                    if currCol == col:
                        isValid = False
                        break
                    if abs(col - currCol) == abs(row - currRow):
                        isValid = False
                        break
                if isValid:
                    placed.append(currCol)
                    dfs(placed)
                    placed.pop()
        dfs([])
        return solutions
        