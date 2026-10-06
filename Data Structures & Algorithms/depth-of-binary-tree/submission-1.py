# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # So we have to go over the tree and get the max possibel depth of it
        # We will iterate over tree using DFS
        # The min depth is one is there a single node and 0 if empty
        # So the depth on this apprioch recusive is 1 + maxdepth of leaf in tree

        # Base case will be return 0
        # We found no more childern in current root of subtree or empty list
        if not root:
            return 0

        
        leftMax = 1 + self.maxDepth(root.left)
        rightMax = 1 + self.maxDepth(root.right)
        res = max(leftMax, rightMax)


        return res

        
        