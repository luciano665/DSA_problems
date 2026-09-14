"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Will use a hashmap OldToCopy of the nodes
        # Since cloning implies creating a new exact node from old
            # Each time we visit a node we need to create a clone of it
        # From there we connect the nodes (undirected <->) does not matter how you connect them
        # This will involve recursive calls at each node

        # BASE CASE EMPTY graph
        if not node:
            return None
        oldToNew = {}

        def clone(node):
            
            # If current nodes copy exist in hashmap we just return it
            if node in oldToNew:
                return oldToNew[node]

            # Node was not cloned yet
            copy = Node(node.val)
            # Add node to hashMap
            oldToNew[node] = copy

            # Go over curr node neighbords (COPY EDGES)
            for nei in node.neighbors:
                # Add the copy of the DFS on current neighbors
                copy.neighbors.append(clone(nei))
            
            # Complete graph is cloned
            return copy
        # DEEP copy of graph
        return clone(node)