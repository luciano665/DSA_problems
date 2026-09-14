# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # We will to do level order traversal on the tree
        # Wil do BFS using a queue
        # Only adding the nodes at the right to the list

        queue = collections.deque()
        queue.append(root)

        res = []
        while queue:
            # Rightmost var
            rightSide = None
            # Current len of queue
            lenL = len(queue)

            # Iterate over queue at some level
            for i in range(lenL):
                # Pop right node at level lenL
                node = queue.popleft()

                # Verify that the a righ node exist
                if node:
                    # Since going from L->R, 
                    # the var righSide will always ends with the right most val
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                # append current right most node at some level
                res.append(rightSide.val)
        
        return res