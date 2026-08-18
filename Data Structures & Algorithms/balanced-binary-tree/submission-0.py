# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.treeHeight(root.left) - self.treeHeight(root.right)) <= 1
        