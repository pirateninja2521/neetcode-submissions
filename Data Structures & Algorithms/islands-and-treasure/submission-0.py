class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        M = len(grid)
        N = len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    queue.append((i, j))
        
        while queue:
            x,y = queue.popleft()

            val = grid[x][y]

            def visit(i, j):
                if (i >= 0 and i < M and j >= 0 and j < N and grid[i][j] == INF):
                    queue.append((i, j))
                    grid[i][j] = val + 1

            visit(x-1, y)
            visit(x+1, y)
            visit(x, y-1)
            visit(x, y+1)

        return 

        
