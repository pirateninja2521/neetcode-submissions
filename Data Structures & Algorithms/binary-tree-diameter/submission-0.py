# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def heightOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        return 1 + max(self.heightOfBinaryTree(root.left), self.heightOfBinaryTree(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        ret = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        height = self.heightOfBinaryTree(root.left) + self.heightOfBinaryTree(root.right)

        return max(ret, height)

