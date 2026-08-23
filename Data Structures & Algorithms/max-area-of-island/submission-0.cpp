class Solution {
private:
    void explore(int i, int j, vector<vector<int>>& grid, int& size) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0) return;
        grid[i][j] = 0;
        size++;
        explore(i-1, j, grid, size);
        explore(i+1, j, grid, size);
        explore(i, j-1, grid, size);
        explore(i, j+1, grid, size);
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int maxSize = 0;
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int size = 0;
                    this->explore(i, j, grid, size);
                    maxSize = max(maxSize, size);
                }
            }
        }
        return maxSize;
    }
    
};
