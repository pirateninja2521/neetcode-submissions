class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        N = len(nums)
        ans = []
        for i in range(N-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = N - 1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return ans
