"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # We will do 2 passes and use hasmap
        # First pass we will copy the old node as keys and the values will be a copy of that node
        # Second pass we will link the copy nodes as the old ones
        # Also need to link the random of the copy to the correct position
        # Finaly we return the head of out deep copy as the new deep copy list

        oldToCopy = {None: None}

        cur = head

        # 1st pass to put all nodes into the hashmap
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # 2nd pass we need to link the copy as the og list
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        # Return deep copy list
        return oldToCopy[head]