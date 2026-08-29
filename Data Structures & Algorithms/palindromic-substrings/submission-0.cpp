class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        // iterate over center
        for(int i = 0; i < s.length(); i++) {
            
            count++;
            // iterate with expanding size
            // odd lengths
            int left = i - 1, right = i + 1;
            while (left >= 0 && right < s.length()) {
                if (s[left] == s[right]) {
                    count++;
                    left--;
                    right++;
                }
                else {
                    break;
                }
            }
            // even lengths
            left = i, right = i + 1;
            while (left >= 0 && right < s.length()) {
                if (s[left] == s[right]) {
                    count++;
                    left--;
                    right++;
                }
                else {
                    break;
                }
            }
        }

        return count;
    }
};
