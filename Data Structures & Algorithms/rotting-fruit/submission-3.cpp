class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> queue;
        int freshcount = 0;
        for(int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 2) {
                    queue.push(make_pair(i, j));
                }
                else if (grid[i][j] == 1) freshcount++;
            }
        }

        int minute = 0;

        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (freshcount && !queue.empty()) {
            int size = queue.size();
            while(size--) {
                auto [x, y] = queue.front();
                queue.pop();
                for(auto [dx, dy] : directions) {
                    if (x+dx >= 0 && x+dx < grid.size() && y+dy >= 0 && y+dy < grid[0].size() && grid[x+dx][y+dy] == 1) {
                        queue.push(make_pair(x + dx, y + dy));
                        grid[x + dx][y + dy] = 2;
                        freshcount--;
                    }
                }
            }
            minute++;
        };
        return freshcount == 0 ? minute: -1;
    }
};
