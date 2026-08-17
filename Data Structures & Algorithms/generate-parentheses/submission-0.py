class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        # i, j: used count for '(' and ')'
        def dfs(i, j, temp: str):
            if len(temp) == 2*n:
                ans.append(temp)
                return
            
            if i==j or j == n:
                dfs(i+1, j, temp + "(")
            elif i == n:
                dfs(i, j+1, temp + ")")
            else:
                dfs(i+1, j, temp + "(")
                dfs(i, j+1, temp + ")")
        
        dfs(0, 0, "")
        return ans