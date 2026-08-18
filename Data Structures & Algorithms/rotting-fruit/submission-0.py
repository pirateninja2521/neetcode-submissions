class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        M = len(grid)
        N = len(grid[0])

        cntFresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1: cntFresh += 1
                elif grid[i][j] == 2: queue.append((i, j))
        
        round = 0
        while queue and cntFresh > 0:
            round += 1
            num = len(queue)
            for _ in range(num):
                x, y = queue.popleft()

                def visit(i, j):
                    nonlocal cntFresh
                    if (i >= 0 and i < M and j >= 0 and j < N and grid[i][j] == 1):
                        grid[i][j] = 2
                        cntFresh -= 1
                        queue.append((i, j))
                visit(x-1, y)
                visit(x+1, y)
                visit(x, y-1)
                visit(x, y+1)
        
        return round if cntFresh == 0 else -1 