class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        def dfs(i, temp):
            ans.append(temp.copy())
            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                temp.append(nums[j])
                dfs(j+1, temp)
                temp.pop()
        
        dfs(0, [])
        return ans

