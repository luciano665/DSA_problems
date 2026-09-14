class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # We will use a DFS and 2 sets to get the (r,c) in grid that are valid in both
        # Traverse up and low row/cols if the can reach to the paci and atlan respectively
        # Have helper function for DFS on current (r,c) and its adjesent ones
        # Will add repectively each valid (r,c) into correct set (pacific, atlantic)

        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevVal):


            # Conditions for invalid cell
            if ((r, c) in visit or r < 0 or c < 0 or
                r == rows or c == cols or heights[r][c] < prevVal):
                return

            # Add valid position to corresping set
            visit.add((r, c))
            # Recursive calls to adjecents location from current (r,c)
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        
        # Traversal from upper and lower sides if valid
        # By col traversal
        for c in range(cols):
            # Upper row to pacific
            dfs(0, c, pac, heights[0][c])
            # Lower row to atlantic
            dfs(rows-1, c, atl, heights[rows-1][c])

        # Traversal from left and right sides if valid
        # By row traversal
        for r in range(rows):
           # Left side to pacific
           dfs(r, 0, pac, heights[r][0])
           # Right side to atlantic
           dfs(r, cols-1, atl, heights[r][cols-1])

        # Will have all valid (r,c) in corresping sets
        # If both r,c in both sets that append that to result
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        # Return the valdid coordinates
        return res


