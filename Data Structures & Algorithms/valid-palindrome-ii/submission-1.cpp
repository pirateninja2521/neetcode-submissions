class Solution {
public:
    bool validPalindrome(string s) {
        int l = 0, r = s.length()-1;

        while (l < r) {
            if (s[l] == s[r]) {
                l++;
                r--;
            }
            else {
                return isPalindrome(s, l, r-1) || isPalindrome(s, l+1, r);
            }
        }
        return true;
    }

private:
    bool isPalindrome(const string& s, int l, int r) {
        while (l < r) {
            if (s[r] != s[l]) return false;
            l++;
            r--;
        }
        return true;
    }
};