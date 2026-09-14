# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Must Use DFS from bottum to top (pre-order traversal)
        # Good nodes are if node-x is > than all vals above
        # Track the max val along current path
        # Global var to keep count of goode nodes


        def dfs(node, maxVal):
        
            # Base case
            if not node:
                return 0


            count = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)

            return count

            return count
    
        return dfs(root, root.val)


        


        

        