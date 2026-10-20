# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We need traverse the tree using recursion
        # Return the LCA from the BST of nodes q and p
        # We know that q and p if we ecounter them the lowest one can be the LCA
        # If q and p are not is same subtree (split happens) then curr node is LCA
        # If in same subtree we keep trtack of current LCA durin traversal
        # leftsub<currnode<rightsub


        # Base case where we have not root 
        if not root or not p or not q:
            return None

        # We need to see where to traverse first alwasy elft (lowest)
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        # Both target ar larger that current root node (go right subtree)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        # p and q split therefore current root node is LCA
        else:
            return root
        



