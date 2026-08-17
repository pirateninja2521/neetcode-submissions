class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])

            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return ans