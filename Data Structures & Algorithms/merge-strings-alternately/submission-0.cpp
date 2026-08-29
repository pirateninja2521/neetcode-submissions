class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int ptr1 = 0, ptr2 = 0;

        string ans;
        while(ptr1 < word1.length() || ptr2 < word2.length()) {
            if (ptr1 < word1.length()) {
                ans += word1[ptr1];
                ptr1++;
            }
            if (ptr2 < word2.length()) {
                ans += word2[ptr2];
                ptr2++;
            }
        }
        return ans;
    }
};