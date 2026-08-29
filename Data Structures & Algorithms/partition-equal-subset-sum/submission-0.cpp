class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2) return false;
        
        // half is the target we want to find for subset sum
        sum /= 2;
        // dp[i][j] : can we sum up to j using subset of nums[:i]
        vector<vector<bool>> dp(nums.size()+1, vector<bool>(sum+1, false));
        // base case
        dp[0][0] = dp[0][nums[0]] = true;
        for(int i = 1; i < nums.size(); i++) {
            for(int j = 0; j <= sum; j++) {
                if (dp[i-1][j]) dp[i][j] = true;
                else if (j >= nums[i] && dp[i-1][j-nums[i]]) dp[i][j] = true;
            }
        }
        return dp[nums.size()-1][sum];
    }
};
