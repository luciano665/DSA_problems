# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # We will need a global list to put the list of each level of the tree
        # We need to to a level order traversal using BFS
        # So BFS uses a queue as DSA but there is a recurisive call also
        # At each step we iterate over the queue and add left and right subnodes to
            # queue
        
        # Init queue structure and append root node
        q = collections.deque()
        q.append(root)

        # global main list
        res = []

        # while the queue is not empty iterate over it
        while q:
            # Need to get length of queue
            lenq = len(q)
            # Init level list
            level = []
            for i in range(lenq):
                currN = q.popleft()

                # if node exists and not null append to level list and append child
                if currN:
                    level.append(currN.val)
                    q.append(currN.left)
                    q.append(currN.right)
            
            # If level is not empty append level list to result list of list
            if level:
                res.append(level)
        
        return res
                    
                


    


