class Solution {
private:
    void explore(int i, int j, vector<vector<char>>& grid) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0') return;
        grid[i][j] = '0';
        explore(i-1, j, grid);
        explore(i+1, j, grid);
        explore(i, j-1, grid);
        explore(i, j+1, grid);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int num = 0;
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    this->explore(i, j, grid);
                    num++;
                }
            }
        }
        return num;
    }
};
