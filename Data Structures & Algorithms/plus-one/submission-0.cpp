class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> ansReverse;
        int plusOne = 1;
        for (int i = digits.size()-1; i >= 0; i--) {
            if (digits[i] + plusOne == 10) {
                ansReverse.push_back(0);
            }
            else {
                ansReverse.push_back(digits[i] + plusOne);
                plusOne = 0;
            }
        }
        if (plusOne) {
            ansReverse.push_back(1);
        }
        reverse(ansReverse.begin(), ansReverse.end());
        return ansReverse;
    }
};
