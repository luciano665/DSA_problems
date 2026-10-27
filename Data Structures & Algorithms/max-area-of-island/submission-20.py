class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # We need to return the max area of island
        # area = all connected 1's horizontally and vertically
        # At each recursion step after we must updete current arae+1
        # then after we update max are if we ecounter max


        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0): 
                return 0
            
            # update land to 0 and increase area of island
            grid[r][c] = 0
            currArea = 1


            for rm, cm in directions:
                currArea += dfs(r + rm, c +cm)
            
            return currArea
            
        

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
            
        
