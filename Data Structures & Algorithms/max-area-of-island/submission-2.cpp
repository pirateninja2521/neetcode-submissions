class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                max_area = max(max_area, dfs(grid, i, j));
            }
        }

        return max_area;
    }

    int dfs(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || i >= grid.size() || j < 0 || j >=grid[0].size() || grid[i][j] == 0) {
            return 0;
        }

        static const vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        grid[i][j] = 0;

        int area = 1;
        for(auto& [dx, dy] : directions) {
            area += dfs(grid, i + dx, j + dy);
        }
        return area;
    }
};
