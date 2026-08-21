class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        ans = 0
        seenChars = set()
        while r < len(s):
            while s[r] in seenChars:
                seenChars.remove(s[l])
                l += 1
            seenChars.add(s[r])
            r += 1
            ans = max(ans, r - l)
        
        return ans