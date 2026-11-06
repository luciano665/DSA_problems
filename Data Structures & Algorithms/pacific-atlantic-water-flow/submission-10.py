class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # We need to traverse from different directions using DFS
        # Corners on left up and bottom right (PAC and ATL oceans)
        # WE keep to sets for each ocean such that similar elemetns in both sets
            # Would mean valid cell coords to return
        # Must only traverse neighbors cells that are lower or ewual in level from current cell

        # Length of grid
        rows = len(heights)
        cols = len(heights[0])


        # Sets
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):

            # We must check invalid cells and return if since we are traversing this in reverse
            # So if current cell-H is < prevH we cant use that cell (it must be  >= prev H)
            if ((r, c) in visit or r < 0 or c < 0 
                or r == rows or c == cols or 
                heights[r][c] < prevHeight):

                return
            
            # Add current r,c to set
            visit.add((r, c))

            # Recursive calls
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        

        # we must call the DFS from both cornes of each side
        # By treversin from row and cols independlty
        # We have to calls since we to sets to populate
        
        # For row traversal
        for r in range(rows):
            # r , 0 (since 0 is firt col) -> direction
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1]) # since we want last col traversal (atl side)
        
        # for col tarvesal
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c]) # last row traversal (bottom corner)



        # Restult array to store cords 
        res = []

        # Iterate over grid
        for r in range(rows):
            for c in range(cols):
                # Check if current cell is both sets = valid cell coord
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
                
    




        