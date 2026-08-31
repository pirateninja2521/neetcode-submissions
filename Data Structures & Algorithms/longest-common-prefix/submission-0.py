class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxLen = min([len(s) for s in strs])

        ans = ""
        for i in range(maxLen):
            chars = set([s[i] for s in strs])
            if len(chars) > 1:
                return ans
            ans += chars.pop()
        
        return ans
        