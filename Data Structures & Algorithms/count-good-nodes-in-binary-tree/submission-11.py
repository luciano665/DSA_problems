# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Must Use DFS from bottum to top (pre-order traversal)
        # Good nodes are if node-x is >= than all vals ont he path to the root
        # Track the max val along current path
        # Update the count on each recurisve call
        

        # Need a helper func for DFS and keep maxVal along path to root
        def dfs(node, maxVal):
        
            # Base case
            if not node:
                return 0
            
            # Count equals 1 if good node else 0
            count = 1 if node.val >= maxVal else 0
            # Update maxVal on current Path
            maxVal = max(maxVal, node.val)
            # Recursive call to left subtree
            count += dfs(node.left, maxVal)
            # Recursive call on right subtree
            count += dfs(node.right, maxVal)


            return count

        return dfs(root, root.val)


        


