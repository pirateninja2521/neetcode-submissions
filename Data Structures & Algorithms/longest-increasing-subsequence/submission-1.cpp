class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        dp.push_back(1);
        int maxlen = 1;
        for (int i = 1; i < nums.size(); i++) {
            int len = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    len = max(1 + dp[j], len);
                }
            }

            maxlen = max(maxlen, len);
            dp.push_back(len);
        }

        return maxlen;
    }
};
