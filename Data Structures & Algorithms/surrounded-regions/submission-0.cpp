class Solution {
private:
    void explore(vector<vector<char>>& board, int i, int j) {
        if (i<0 || j<0 || i>=board.size() || j>=board[0].size() || board[i][j] != 'O') return;
        board[i][j] = '@';
        explore(board, i-1, j);
        explore(board, i+1, j);
        explore(board, i, j-1);
        explore(board, i, j+1);
    }
public:
    void solve(vector<vector<char>>& board) {
        for(int i = 0; i < board.size(); i++) {
            for(int j = 0; j < board[0].size(); j++) {
                if (i == 0 || j == 0 || i == board.size()-1 || j == board[0].size()-1) {
                    explore(board, i, j);
                }
            }
        }

        for(int i = 0; i < board.size(); i++) {
            for(int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '@') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};
