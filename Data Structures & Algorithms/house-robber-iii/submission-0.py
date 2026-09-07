# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0, 0
            
            left1, left2 = dfs(root.left)
            right1, right2 = dfs(root.right)

            return root.val + left2 + right2, max(left1, left2) + max(right1, right2)
        
        val1, val2 = dfs(root)

        return max(val1, val2)
        