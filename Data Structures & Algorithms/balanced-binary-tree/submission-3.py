# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # We need to use DFS to get the height of the tree
        #Durint traversal we will check is balanced 
            # Such that if leftH-reightH > 1 = not balanced
        # Return the height as always but the main func return Bool if is balanced or not
        self.isBalancedT = True

        def dfs(curr):

            if not curr:
                return 0

            leftH = dfs(curr.left)
            rightH = dfs(curr.right)

            if leftH - rightH > 1 or rightH-leftH > 1:
                self.isBalancedT = False

            return 1 + max(leftH, rightH)

        dfs(root)
        return self.isBalancedT