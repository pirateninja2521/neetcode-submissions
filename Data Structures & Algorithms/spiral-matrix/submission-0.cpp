class Solution {
public:
    void spiralLoop(int idx, vector<vector<int>>& matrix, vector<int>& ans) {
        const int& M = matrix.size();
        const int& N = matrix[0].size();
        if(2 * idx + 1 == M) {
            for(int j = idx; j < N - idx; j++) {
                ans.push_back(matrix[idx][j]);
            }
            return;
        }
        if(2 * idx + 1 == N) {
            for(int i = idx; i < M - idx; i++) {
                ans.push_back(matrix[i][idx]);
            }
            return;
        }
        // else normal case
        for(int j = idx; j < N - idx; j++) {
            ans.push_back(matrix[idx][j]);
        }
        for(int i = idx + 1; i < M - idx - 1; i++) {
            ans.push_back(matrix[i][N - 1 - idx]);
        }
        for(int j = N-1-idx; j >= idx; j--) {
            ans.push_back(matrix[M - 1 - idx][j]);
        }
        for(int i = M-1-idx-1; i > idx; i--) {
            ans.push_back(matrix[i][idx]);
        }
        return;

    }
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        const int& M = matrix.size();
        const int& N = matrix[0].size();
        vector<int> ans;
        for(int i = 0; 2 * i < min(M, N); i++) {
            spiralLoop(i, matrix, ans);
        }
        return ans;
    }
};
