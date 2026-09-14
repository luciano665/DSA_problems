# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # We need to check if the 2 trees are the same
        # We will traverse the trees using DFS
        # We must check at each recursive step if nodes are equal or null

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        
        else:
            return False
