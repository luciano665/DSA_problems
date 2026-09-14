# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        # We will use a DFS and need to compare that current node L and R childs
            # L child is < current node and R child > current node


        def dfs(node, left, right):

            # Base case
            if not node:
                return True

            if not(left < node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)





        return dfs(root, float("-inf"), float("inf"))
