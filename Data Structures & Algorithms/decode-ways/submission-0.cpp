class Solution {
public:
    int numDecodings(string s) {
        vector<int> dp(s.length()+1, 0);

        // invalid string
        if (s[0] == '0') return 0;
        dp[0] = dp[1] = 1;

        for(int i = 2; i <= s.length(); i++) {
            if (s[i-1] != '0') {
                dp[i] += dp[i-1];
            }
            int num = (s[i-2] - '0') * 10 + (s[i-1] - '0');
            if (s[i-2] != '0' && num <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[s.length()];
    }
};
