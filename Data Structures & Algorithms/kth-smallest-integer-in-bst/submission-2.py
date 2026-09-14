# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # We will use in-order traversal
        # Since we need the kth smalles element (1-index)
        # We will use a stack like recursive calls (not using recursion)
        # Since BST we know vals on node on the left < node < right


        stack = []

        curr = root

        # Start traversal
        while stack or curr:

            # Curr node is not null
            while curr:
                stack.append(curr)
                curr = curr.left

            # We will have appended all the left subtree
            curr = stack.pop()
            # Update smallest count
            k -= 1 

            if k == 0:
                return curr.val

            # Else we are allowed to move to the right
            curr = curr.right


