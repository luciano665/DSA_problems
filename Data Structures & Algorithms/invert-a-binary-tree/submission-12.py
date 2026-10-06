# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # We will use DFS to go over the tree nodes
        # We will swap value from left to right and vicevars
        # Then we recuirsevly traver a kepp changing
        # The key is on first swap node values and then recusively call to proper directions

        # Base case not root
        if not root:
            return None

        # Swap happens here
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive call starting at root.left and not as nomrally root right
        # Since the og root.right is currently the right.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root