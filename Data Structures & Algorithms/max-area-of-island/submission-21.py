class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # We need to return the max area of island
        # area = all connected 1's horizontally and vertically
        # At each recursion step after we must updete current arae+1
        # then after we update max are if we ecounter max

        # We set row and cols len for treversal use
        rows = len(grid)
        cols = len(grid[0])
        # global var for storing max area encounter and maxA to return
        maxArea = 0

        # Horizontal and vertical direction to move at each island encountered 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            # If we found an invalid coordinate or move in the grid we return 0 no more are to increment
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0): 
                return 0
            
            # update land to 0 (sink)
            grid[r][c] = 0

            # Set current area to 1 of explored island
            currArea = 1


            for rm, cm in directions:
                # at each recurisve call in encountered area we update curr Area of connected island
                # if avialable
                currArea += dfs(r + rm, c +cm)
            
            # return currArea of islands 
            return currArea
            
        

        # Start iteration over grid
        for r in range(rows):
            for c in range(cols):
                # If encounter an island we call dfs traversal
                if grid[r][c] == 1:
                    # Update max area if we found a greater one from current Max
                    maxArea = max(maxArea, dfs(r, c))
        
        # Return the max Area
        return maxArea
            
        
