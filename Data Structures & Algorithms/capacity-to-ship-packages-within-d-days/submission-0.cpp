class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int low = *max_element(weights.begin(), weights.end());
        int high = accumulate(weights.begin(), weights.end(), 0);

        int result = high;
        while (low <= high) {
            int target = (low + high) / 2;

            int day = 1, curr = 0;
            for (int weight:weights) {
                if (curr + weight > target) {
                    curr = weight;
                    day++;
                }
                else curr += weight;
            }

            if (day > days) {
                low = target + 1;
            }
            else {
                result = target;
                high = target - 1;
            }
        }
        return result;
    }
};