class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0, start = 0;
        unordered_set<char> seen;
        for (int end = 0; end < s.length(); end++) {
            while(seen.contains(s[end])) {
                seen.erase(s[start]);
                start++;
            }
            seen.insert(s[end]);
            ans = max(ans, end - start + 1);
        }
        return ans;
    }
};
