class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        prevMax, curMax = 0, 0
        prevMaxWithoutZero, curMaxWithoutZero = 0, 0

        for i in range(len(nums)):
            if i != len(nums)-1:
                prevMax, curMax = curMax, max(prevMax + nums[i], curMax)
            if i != 0:
                prevMaxWithoutZero, curMaxWithoutZero = curMaxWithoutZero, max(prevMaxWithoutZero + nums[i], curMaxWithoutZero)
        
        return max(curMaxWithoutZero, curMax)
