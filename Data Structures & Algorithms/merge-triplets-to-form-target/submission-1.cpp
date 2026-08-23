class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        vector<int> merged_triplets = {0, 0, 0};

        for (const auto& triplet : triplets) {
            if (triplet[0] > target[0] ||
                triplet[1] > target[1] ||
                triplet[2] > target[2]) {
                continue;
            }
            for (int i = 0; i < 3; i++) {
                merged_triplets[i] = max(merged_triplets[i], triplet[i]);
            }
        }
        return merged_triplets == target;
    }
};
