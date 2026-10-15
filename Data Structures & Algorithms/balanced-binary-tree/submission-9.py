# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # We can use DFS to traverse the tree
        # Each time we compute height of subtrees
        # We have a global var to constant update to see if is balanced or not
            # At each subtree

        # A balanced tree is valid if left - right <= 1

        self.isBalanced = True

        def dfs(node):

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)


            if abs(left - right) > 1:
                self.isBalanced = False

            return 1 + max(left, right)

        
        dfs(root)
        return self.isBalanced

            