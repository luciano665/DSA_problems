# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # We need return all nodes values avialable RSV
        # A valid node RSV is the last node at each level
        # There fore we cna iterate over tree using BFS
        # Keep track of all a temp list and keep only last value
        # At each final travelsal of a level we add last element to rest list


        res = []

        q = collections.deque()
        q.append(root)

        # traverse the queue
        while q:

            lenq = len(q)
            level = []
            for i in range(lenq):
                node = q.popleft()
                # Get nodes from q and append sub nodes
                if node:
                    # append node val to level
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            # We must chekc that if level list not empty we add last node to res 
            if level:
                res.append(level[-1]) # last element only valid RVS

        return res
