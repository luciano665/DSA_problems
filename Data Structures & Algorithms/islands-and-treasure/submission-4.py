class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # -1 (water-cant traverse), 0 (chest), INF (land)
        # We will BFS for level by level from nearest chest found
        # Start normal r,c iteration over grid until find a chest
            # Call to BFS
        # Keep track on BFS of current (r, c) visited level by level
        # Then we adjecents cells from it (all directrions)

        rows, cols = len(grid), len(grid[0])
        visited = set()
        # We need a queue  for BFS
        queue = deque()

        # Helper iteration function using BFS
        def addCell(r, c):
            # If encounter wall or invalid coord
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == -1):
                return

            # Update queue and set of visited
            visited.add((r, c))
            queue.append([r, c])


        # iteration over grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        dist = 0
        # Start of BFS on current chest at curr level
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                # current [r][c] is set to minDist-level from chest
                grid[r][c] = dist
                # Recursive calls
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            # Update dist for next level
            dist += 1




        