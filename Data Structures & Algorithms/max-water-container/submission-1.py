class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)

        i = 0
        j = N-1

        ans = 0
        while i < j:
            ans = max(ans, min(heights[i], heights[j]) * (j-i) )

            if heights[i] == heights[j]:
                i += 1
                j -= 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return ans