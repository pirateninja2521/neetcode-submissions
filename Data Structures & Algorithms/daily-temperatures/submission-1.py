class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prevIndex = stack.pop()
                ans[prevIndex] = index - prevIndex
            stack.append(index)
        
        while stack:
            ans[stack.pop()] = 0
        return ans