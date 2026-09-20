class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }

        return count;

    }

    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || i >= grid.size() || j < 0 || j >=grid[0].size()) return;
        if (grid[i][j] == '0') return;

        set<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        grid[i][j] = '0';
        for(auto& [dx, dy] : directions) {
            dfs(grid, i + dx, j + dy);
        }
    }
};
