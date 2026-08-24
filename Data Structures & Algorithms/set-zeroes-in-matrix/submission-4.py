class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        rowZero = False
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True

        for row in range(1, M):
            for col in range(1, N):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(M):
                matrix[row][0] = 0
        if rowZero:
            for col in range(N):
                matrix[0][col] = 0