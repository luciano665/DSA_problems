class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # We will perfrom a DFS on the graph nodes and edges
        # We need check tha graph is a valid tree
            # No cycles in graph
            # The # of edges > n - 1 nodes
        # We need adjecent list to have the node and its edges (connections)
        # We will DFS starting from 0 node, each time a node is not in the visit set 
            # Was visited before ther is no cycle
        # Also the DFS call will have thwe current node and it's prev sych that we dont have false cycle positives

        # Base case
        if len(edges) > n-1:
            return False

        # Create adjecent list
        adjL = [[] for _ in range(n)]
        for v, u in edges:
            adjL[u].append(v)
            adjL[v].append(u)

        # Init our visit set
        visit = set()

        def dfs(node, prev):

            # Cycle is detected
            if node in visit:
                return False

            # Update visit set
            visit.add(node)
            for newn in adjL[node]:
                # Handle false cycle positives
                if newn == prev:
                    continue
                # Recursive call to visit the other nodes DFS
                if not dfs(newn, node):
                    return False
            # We have a valid tree
            return True 

        # return result of dfs (-1 bc there is no prev node yet)
        # visit set should be same the number of nodes we have
        return dfs(0, -1) and len(visit) == n

