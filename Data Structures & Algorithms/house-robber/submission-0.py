class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prevMax, curMax = 0, 0

        for num in nums:
            prevMax, curMax = curMax, max(prevMax + num, curMax)
        
        return curMax
            
        