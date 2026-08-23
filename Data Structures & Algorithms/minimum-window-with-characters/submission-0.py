class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t)
        counterS = Counter()
        l = 0
        ans = None
        for r in range(len(s)):
            counterS[s[r]] += 1
            if counterT <= counterS:
                while counterS[s[l]] > counterT[s[l]]:
                    counterS[s[l]] -= 1
                    l += 1
                
                if not ans or len(ans) > r - l + 1:
                    ans = s[l:r+1]
        
        if not ans:
            ans = ""
        return ans
                