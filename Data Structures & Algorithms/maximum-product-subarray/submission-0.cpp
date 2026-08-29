class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) return -1;

        int prevMax = nums[0], prevMin = nums[0], historyMax = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            int tempMax = nums[i] * prevMax, tempMin = nums[i] * prevMin;
            prevMin = min({tempMax, tempMin, nums[i]});
            prevMax = max({tempMax, tempMin, nums[i]});
            historyMax = max(historyMax, prevMax);
        }
        return historyMax;
        
    }
};
