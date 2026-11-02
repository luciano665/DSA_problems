"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Return a deep copy of given graph -> Cloning the entire graph
        # Graph is represented as adj-list = list of lists
        # 1-indexed each element in main list is the connection of the current to to other node
        # Node range alwasy from 1 to N
        # if list has not lists inside we return single list but if only empty list and empty 
            # list inside too ther ea single node 1
        # Recurisvely using DFS need to map nodes to their cloned nodes
        # At each dfs step we create a new node with current node val
            # Recurisve step will be go to current nodes neighbors and try to clone them
        # After that, we add them to the neighbors list
        # Base case will be we we alridy visit a node

        # Init hashmap to map oldToNew
        oldToNew = {}

        # dfs function to traverse graph to clone
        def dfs(curr):

            # Base case we alraedy visited this node
            if curr in oldToNew:
                return oldToNew[curr]
            

            # make the copy of current node as new node with curr node val and update map
            copy = Node(curr.val)
            oldToNew[curr] = copy
            
            # for loop to go over neighbors or current node and we add them into map
            for ng in curr.neighbors:
                copy.neighbors.append(dfs(ng))
            
            # retrurn the copy
            return copy
        
        # Return copy or lese nothing was given
        return dfs(node) if node else None
            
            

        


        