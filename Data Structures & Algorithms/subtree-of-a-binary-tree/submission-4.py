# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Use DFS for traversing the tree until we find the root of the tree 
        # That matches the root of the subtree
        # We traverse from root in tree and subtree to see if the match

        # Edge cases

        # Empty tree-main
        if not root:
            return False
        # Empty subtree
        if not subRoot and root:
            return True

        
        if self.sameTree(root, subRoot):
            return True
        
        # Current SubTree was not subTree got to next SubStree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
        # Helper Function to see if subtree is in tree
    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2:
            return True

        if root1 and root2 and root1.val == root2.val:
            return (self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right))
        
        return False


