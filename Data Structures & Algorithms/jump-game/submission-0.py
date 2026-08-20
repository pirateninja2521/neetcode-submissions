class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1: return True

        goal = N-1
        for i in range(N-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

        