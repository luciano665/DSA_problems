class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        # So we need to recursively traverse the 2D grid that represents a graph
        # Using DFS when we encounter a 1 and check if valid island
        # We mark vsisited 1 as 0 to no revist again
        # We must keep track of visited nodes on grid]
        # Each DFS call corresponfs to one island only
        # On DFS we need to recursively visit from encouter node '1'
            # all directions (up, down, right, left)

        # Need to have directions all of them for traversing if we encouter a island
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # get length of rows and cols
        rows = len(grid)
        cols = len(grid[0])

        # global var to keerp track of # of islands
        islands = 0

        def dfs(r, c):

            # base case we return if we found a '0' not more 1 surrounded
            if (r < 0 or c < 0 or  r >= rows or c >= cols or grid[r][c] == '0'):
                return;
            
            # mark the current valid 1 to 0 -> sink island
            grid[r][c] = '0'

            # keep traversing other direction from current node
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        # Need to start going over the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                #   Check current element if 1
                if grid[i][j] == '1':
                    # Call dfs from here
                    dfs(i, j)
                    islands += 1
        
        return islands




