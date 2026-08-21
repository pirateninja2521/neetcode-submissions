class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)

        ans = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            charCount[s[r]] += 1
            maxf = max(maxf, charCount[s[r]])

            while (r - l + 1) - maxf > k:
                charCount[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans