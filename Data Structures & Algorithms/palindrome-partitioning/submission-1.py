class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Will use backtracking to solve problem
        # We will create every possible partion from s
        # And check if those partitions are valid palindromes
            # If true we appended to th list as a list
        # Each partition of S as first desicions level then from there
        # On each path (partition above), we take the partition from the reminder chars on S
        # Must check that each partition on each path the valid palindromes


        res = []
        part = [] # for current partition

        # Will use DFS for traversing the possible paths
        def dfs(i):

            # Base Case: we are out of bounds
            # Have valid part on a path and is a palidrome
            if i >= len(s):
                res.append(part.copy())
                return

            # Start traversing s to get partitions
            # J acts as the right pointer on substring
            for j in range(i , len(s)):
                # Check if every poss substr is a palindrome
                if self.isPalin(s, i, j):
                    # Append current partition from i to j
                    part.append(s[i: j + 1])
                    # Recursive call to all possible additional partitions using DFS
                    dfs(j + 1)
                    # We Pop recent str added part from stack
                    part.pop()
            
        dfs(0)
        return res

    
    # Need a helper function to check palindrome
    def isPalin(self, s, l, r):

        while l < r:
            # Current ends dont match = not palindrome
            if s[l] != s[r]:
                return False
            l , r = l + 1, r - 1

        return True

        

            
