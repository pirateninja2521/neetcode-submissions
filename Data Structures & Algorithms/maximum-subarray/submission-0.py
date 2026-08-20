class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        PrevMaxSubArray = nums[0]

        ans = PrevMaxSubArray
        for i in range(1, len(nums)):
            PrevMaxSubArray = max(nums[i], nums[i] + PrevMaxSubArray)

            ans = max(ans, PrevMaxSubArray)
        
        return ans