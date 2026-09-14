# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Base Case
        if not preorder or not inorder:
            return None

        # Get root values from both arrays
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # Get all elements of leftsubtree
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        # Get array elements of the right Subtree
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

       