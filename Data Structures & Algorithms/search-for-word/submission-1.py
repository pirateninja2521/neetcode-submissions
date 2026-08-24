class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        visited = [[0 for _ in range(N)] for _ in range(M)]
        found = False
        def dfs(i, j, index = 0):
            nonlocal found, visited
            if found:
                return
            if index == len(word):
                found = True
                return
            if not 0 <= i < M or not 0 <= j < N or visited[i][j] or word[index] != board[i][j]:
                return
            
            visited[i][j] = 1
            dfs(i-1, j, index+1)
            dfs(i+1, j, index+1)
            dfs(i, j-1, index+1)
            dfs(i, j+1, index+1)
            visited[i][j] = 0
        
        for i in range(M):
            for j in range(N):
                dfs(i, j, 0)
        return found

