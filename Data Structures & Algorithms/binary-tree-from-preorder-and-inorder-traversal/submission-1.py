class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map values to their indices in the inorder array for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. Keep track of our current root in the preorder array
        self.preorder_index = 0
        
        # 3. Helper function uses boundaries instead of slicing arrays
        def build(left, right):
            # Base case: if left > right, there are no nodes to process
            if left > right:
                return None
            
            # The next element in preorder is always the root of the current subtree
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_val)
            
            # Find where this root is in the inorder array to split left/right boundaries
            mid = inorder_map[root_val]
            
            # Build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        # Start the recursion with the boundaries of the full inorder array
        return build(0, len(inorder) - 1)