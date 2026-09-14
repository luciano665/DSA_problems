# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        # Hashmap to store the index and val of inorder
        # So we have O(n) time
        
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.preOrdIdx = 0

        def dfs(l, r):

            if l > r:
                return None

            # Get root values in both arrays
            root_val = preorder[self.preOrdIdx]
            self.preOrdIdx += 1
            # Set root of tree
            root = TreeNode(root_val)

            mid = indices[root_val]
          

            root.left = dfs(l, mid-1) # All left vals on the left of mid (leftSubtree)
            root.right = dfs(mid +1, r) # All right vals on the right of mid (rightSubtree)


            return root

        return dfs(0, len(inorder) - 1)









