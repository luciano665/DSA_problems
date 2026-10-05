# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        # Will use a DFS to traverse the tree
        # We will swap edges from left into right recursively
        # Swe explore from left node

        # Base case we are at root
        if not root:
            return None

        #Swaap of edges
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive call to left node from root
        self.invertTree(root.left) # This will be recursive call to orginal node at right
        self.invertTree(root.right) # Invert subtree original into left

        return root