# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def maxPathSumRoot(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if not root:
                return 0
            if root and not root.left and not root.right:
                ans = max(ans, root.val)
                return root.val
            else:
                maxPathSumRootLeft, maxPathSumRootRight = max(maxPathSumRoot(root.left), 0), max(maxPathSumRoot(root.right), 0)
                ans = max(ans, root.val + maxPathSumRootLeft +  maxPathSumRootRight)
                
                return root.val + max(maxPathSumRootLeft, maxPathSumRootRight)
        
        maxPathSumRoot(root)
        return ans