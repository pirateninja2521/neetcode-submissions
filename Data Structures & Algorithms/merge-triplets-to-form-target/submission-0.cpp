class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        vector<int> ans = {0, 0, 0};

        for (const auto& triplet : triplets) {
            if (triplet[0] > target[0] ||
                triplet[1] > target[1] ||
                triplet[2] > target[2]) {
                continue;
            }
            for (int i = 0; i < 3; i++) {
                ans[i] = max(ans[i], triplet[i]);
            }
        }
        return ans == target;
    }
};
