class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # We will use a DFS approach 
        # Will traverse the complette grid each row and each columin and call the dfs
        # Will check if current grid is not 0
        # Change current loc at grid as 0 (as counted to not traversed again)
        # Count set to 1  and recursive calls to all positions (horizontally and vertically to it)
        # Return the count and get the max of current max area and last dfs call

        rows , cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r , l):
            # base case 
            if (r < 0 or r == rows or l < 0 or l == cols or grid[r][l] == 0 or (r, l) in visited ):
                return 0 

            # Update count and visited coords
            count = 1
            visited.add((r, l))

            # Recursive calls
            count += dfs(r, l+1)
            count += dfs(r, l-1)
            count += dfs(r+1, l)
            count += dfs(r-1, l)

            return count

        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea

