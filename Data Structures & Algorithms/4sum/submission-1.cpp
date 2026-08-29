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

                int ptr1 = j + 1, ptr2 = nums.size()-1;
                while (ptr1 < ptr2) {
                    int num3 = nums[ptr1], num4 = nums[ptr2];
                    long long sum = (long long) nums[i] + nums[j] + num3 + num4; 
                    if ( sum == newTarget) {
                        answers.push_back({nums[i], nums[j], nums[ptr1], nums[ptr2]});
                        while (nums[++ptr1] == num3 && ptr1 < ptr2);
                        while (nums[--ptr2] == num4 && ptr1 < ptr2);
                    }
                    else if (sum < newTarget) {
                        ptr1++;
                    }
                    else {
                        ptr2--;
                    }
                }
            }
        }
        return answers;
    }
};