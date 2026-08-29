class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.length()+1, false);

        // whether s[0:i+1] is a valid substring
        dp[0] = true;


        // dp[j] true if any of dp[i] is true and s[i+2:j] in wordDict
        for (int i = 1; i <= s.length(); i++) {
            for (string& word: wordDict) {
                if (i >= word.length() && dp[i - word.length()] && s.substr(i - word.length(), word.length()) == word) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp.back();
    }
};
