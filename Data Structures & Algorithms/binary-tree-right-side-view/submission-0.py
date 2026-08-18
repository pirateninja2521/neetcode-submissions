# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        ans = []
        queue = deque([root])

        while queue:
            ans.append(queue[0].val)
            
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
            
        return ans

