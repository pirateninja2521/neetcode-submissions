# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesWithMaxVal(self, root: TreeNode | None, maxVal: int) -> int:
        if root is None: return 0
        if root.val >= maxVal: return 1 + self.goodNodesWithMaxVal(root.left, root.val) + self.goodNodesWithMaxVal(root.right, root.val)
        else: return self.goodNodesWithMaxVal(root.left, maxVal) + self.goodNodesWithMaxVal(root.right, maxVal)

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesWithMaxVal(root, root.val)

    
        