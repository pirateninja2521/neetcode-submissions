class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 0: return [[]]
        
        ans = []
        for i, num in enumerate(nums):
            perms = self.permute(nums[:i] + nums[i+1:])
            for p in perms:
                ans.append([num] + p)
        return ans