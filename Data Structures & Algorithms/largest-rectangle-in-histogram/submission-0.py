class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxArea = 0
        
        # (height, index)
        stack = []
        for index, height in enumerate(heights):
            prevIndex = float("inf")
            while stack and stack[-1][0] > height:
                prevHeight, prevIndex = stack.pop()
                maxArea = max(maxArea, prevHeight * (index-prevIndex))

            if not stack or stack[-1][0] < height:
                stack.append((height, min(index, prevIndex)))
        
        return maxArea
# maxArea = 7       
# [(1, 0), (2,), (4, 5), (0, 6)]


# stack for incoming heights
# [7] -> [1]

# [(7,0),(8, 1)] -> [(6, 2)] --> [(0, 3)]
# recognize we we have rectanges higher than 6
# 7: 0-1 -> 14
# 8: 1-1 -> 8
# pop out prevHeight, prevPos
# can form rectangle of height prevHeight and wiedth currPos-prevPos

# [(6, 0)] -> [(0, 3)]
# 6: 0-2 -> 18
#[(0,0)]
