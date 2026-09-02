class Solution:
    def totalNQueens(self, n: int) -> int:
        placed_queens = []
        count = 0
        def dfs(index):
            nonlocal count
            if index == n:
                count += 1
                return
            for pos in range(n):
                if pos not in placed_queens:
                    valid = True
                    for prevIndex, prevPos in enumerate(placed_queens):
                        if abs(prevIndex - index) == abs(prevPos - pos):
                            valid = False
                            break
                    if valid:
                        placed_queens.append(pos)
                        dfs(index + 1)
                        placed_queens.pop()
    
        dfs(0)

        return count
                    
