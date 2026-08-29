class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        long long newTarget = (long long) target;
        vector<vector<int>> answers;
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i+1; j < nums.size(); j++) {
                if (j > i+1 && nums[j] == nums[j-1]) continue;

                int left = j + 1, right = nums.size()-1;
                while (left < right) {
                    int num3 = nums[left], num4 = nums[right];
                    long long sum = (long long) nums[i] + nums[j] + num3 + num4; 
                    if ( sum == newTarget) {
                        answers.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[++left] == num3);
                        while (left < right && nums[--right] == num4);
                    }
                    else if (sum < newTarget) {
                        left++;
                    }
                    else {
                        right--;
                    }
                }
            }
        }
        return answers;
    }
};