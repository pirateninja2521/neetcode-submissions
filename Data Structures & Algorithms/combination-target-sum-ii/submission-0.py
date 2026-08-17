class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        N = len(candidates)

        def dfs(i, temp, total):
            if total == target:
                ans.append(temp.copy())
                return
            if i > N or total > target:
                return
            
            for j in range(i, N):
                if total + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                temp.append(candidates[j])
                dfs(j+1, temp, total + candidates[j])
                temp.pop()

        dfs(0, [], 0)
        return ans