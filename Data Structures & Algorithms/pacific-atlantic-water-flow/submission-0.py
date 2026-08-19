class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])
        pacific = [ [0] * N for _ in range(M)]
        atlantic = [ [0] * N for _ in range(M)]

        queuePacific = deque()
        queueAtlantic = deque()
        for i in range(M):
            pacific[i][0]= 1
            queuePacific.append((i, 0))
            atlantic[i][N-1] = 1
            queueAtlantic.append((i, N-1))

        for i in range(N):
            pacific[0][i] = 1
            queuePacific.append((0, i))
            atlantic[M-1][i] = 1
            queueAtlantic.append((M-1, i))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queuePacific:
            x, y = queuePacific.popleft()
            for dx, dy in directions:
                if (x + dx >= 0 and x + dx < M and y + dy >= 0 and y + dy < N and heights[x][y] <= heights[x + dx][y + dy] and pacific[x + dx][y + dy] == 0):
                    pacific[x + dx][y + dy] = 1
                    queuePacific.append((x + dx, y + dy))
        
        while queueAtlantic:
            x, y = queueAtlantic.popleft()
            for dx, dy in directions:
                if (x + dx >= 0 and x + dx < M and y + dy >= 0 and y + dy < N and heights[x][y] <= heights[x + dx][y + dy] and atlantic[x + dx][y + dy] == 0):
                    atlantic[x + dx][y + dy] = 1
                    queueAtlantic.append((x + dx, y + dy))
        
        ans = []
        for i in range(M):
            for j in range(N):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans
        

        