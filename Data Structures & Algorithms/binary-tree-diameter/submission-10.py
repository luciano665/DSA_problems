# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # We need to travers using DFS the binary tree
        # Find the diameter which is the longest path you can get between 2 nodes
        # We need to keep track of visted nodes and get len of it on each recursive
        # So in dfs the the diameter is sum of left and right height + 1 (for root)

        self.res = 0

        # Nested helper for recursive dfs
        def dfs(currN):

            if not currN:
                return 0
            
            left = dfs(currN.left)
            right = dfs(currN.right)

            # Calculate the maxD up to know
            self.res = max(self.res, left + right)

            # Return the height + 1 of current subtree
            # Such that parent node can use it
            return 1 + max(left, right)

        # Recurisve call from root + 1 to return height
        dfs(root)
        return self.res
    