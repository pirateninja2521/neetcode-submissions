# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)

            if val == "N":
                return None
            node = TreeNode((int(val)))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()