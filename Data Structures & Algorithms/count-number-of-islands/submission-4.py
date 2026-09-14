class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # We can use BFS to traverse the 2D griid
        # In order to find a valid island
        # Must return the # of islands

        # We will need a counter for islands 
        # A set to keep the current coordinated on grid of visited islands


        # Base case for empty grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):

            # Unit queuq
            queue = collections.deque()
            # Add current visited coord
            visited.add((r, c))
            queue.append((r, c))

            # Adjecnet directions
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            #start traversal
            while queue:
                row , col = queue.popleft()

                for dr, cr in directions:
                    nr, nc = row + dr, col + cr

                    # Check conditions
                    if (nr in range(rows) and nc in range(cols)
                        and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # Start the iteration of the islands on the grid row/col
        for r in range(rows):
            for c in range(cols):
                # Need to check if row and col is 1
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    #Update counter 
                    islands += 1

        return islands

