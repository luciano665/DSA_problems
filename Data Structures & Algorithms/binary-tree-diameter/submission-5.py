# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # We can use DFS as for the height 
        # As usual + 1 after to update
        # We need to update the max D of the sum of the left and right 
        # Calcualte the diameter at each node 
        # Get only max diameter of prev diameter calculated

        self.res = 0

        def dfs(curr):

            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # Calcluate the maxD
            self.res = max(self.res, left + right)

            # Return the height
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
    

        