class Solution {
public:
    void rotateCorners(const int& i, const int& j, vector<vector<int>>& matrix) {
        const int N = matrix.size();
        int temp = matrix[i][j];
        matrix[i][j] = matrix[N-1-j][i];
        matrix[N-1-j][i] = matrix[N-1-i][N-1-j];
        matrix[N-1-i][N-1-j] = matrix[j][N-1-i];
        matrix[j][N-1-i] = temp;
    }

    void rotate(vector<vector<int>>& matrix) {
        const int N = matrix.size();
        for (int i = 0; i < (N+1)/2; i++) {
            for (int j = 0; j < N/2; j++) {
                rotateCorners(i, j, matrix);
            }
        }
    }
};


// i, j
// j, N-1-i
// N-1-i, N-1-j
// N-1-j, i