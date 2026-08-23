class Solution {
public:
    int digitsSum(int n) {
        int ans = 0;
        while (n) {
            int lastDigit = n % 10;
            ans += (lastDigit * lastDigit);
            n /= 10;
        }
        return ans;
    }
    bool isHappy(int n) {
        unordered_set<int> seenNumbers;
        while (n > 1) {
            if (seenNumbers.contains(n)) {
                return false;
            }
            seenNumbers.insert(n);
            n = digitsSum(n);
        }
        return true;
    }
};
