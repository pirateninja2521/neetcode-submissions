class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        current = []
        def dfs(current, index):
            if len(current) == k:
                ans.append(current.copy())
                return
            if index > n:
                return

            dfs(current, index + 1)
            current.append(index) 
            dfs(current, index + 1)
            current.pop()

        dfs(current, 1)
        return ans
        