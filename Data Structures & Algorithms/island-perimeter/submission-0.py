class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        def explore(i, j):
            nonlocal perimeter

            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                perimeter += 1
                return
            if grid[i][j] == -1:
                return
            grid[i][j] = -1
            
            explore(i-1, j)
            explore(i+1, j)
            explore(i, j-1)
            explore(i, j+1)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    explore(i, j)
                    return perimeter