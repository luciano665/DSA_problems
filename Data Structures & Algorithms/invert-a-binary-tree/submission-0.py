# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # We need to swap right left children and then use recursion 
        # So we can inver the next subtrees
        # Will use DFS doesnt matter if pre-order

        # Base case
        if not root:
            return None

        # Swapping 
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root