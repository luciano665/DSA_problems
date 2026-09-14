# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Level order traversal == BFS
        # Need a list to store lists at each level
        # BFS starts and the root and visits the left and right child
            # That for each level
        # We need a queue for BFS 
        # Must iterate at each level up to len of curr queue
        

        # INIT QUEUE
        queue = collections.deque()
        queue.append(root)

        res = []

        while queue:
            lenOfQ = len(queue)
            listLev = []

            # We create the curr les of vals at given level
            for i in range(lenOfQ):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    listLev.append(node.val)

            # Append list level into the list of levels
            if listLev:
                res.append(listLev)

        return res







        