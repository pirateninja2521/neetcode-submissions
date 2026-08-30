class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        ans = len(nums) + 1
        for r, num in enumerate(nums):
            currSum += num
            if currSum >= target:
                while currSum - nums[l] >= target:
                    currSum -= nums[l]
                    l += 1
                ans = min(ans, r - l + 1)
        return ans if ans != len(nums) + 1 else 0
