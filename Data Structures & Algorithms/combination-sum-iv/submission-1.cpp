class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // dp[i][j]: combinations for using numbers from s[:i] sum up to j

        vector<int> dp(target+1, 0);
        // base case
        dp[0] = 1;

        for (int total = 1; total <= target; total++) {
            for (int num:nums) {
                if (total >= num) {
                    dp[total] += dp[total - num];
                }
            }
        }
        return dp[target];
    }
};