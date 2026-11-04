class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Multi-source BFS:
        # Start from ALL treasure cells (0) simultaneously.
        # Explore the grid level by level.
        # Each level represents the distance from the nearest treasure.

        rows = len(grid)
        cols = len(grid[0])

        # Queue stores coordinates of cells waiting to be processed.
        q = deque()

        # Keep track of cells already added to the queue.
        # Prevents revisiting cells and assigning longer distances.
        visited = set()

        def addCell(r, c):

            # Ignore cells that:
            # - Are outside the grid
            # - Have already been visited
            # - Are walls (-1), which cannot be traversed
            if (min(r, c) < 0 or r == rows or c == cols
                or (r, c) in visited or grid[r][c] == -1):
                return

            # Mark the cell visited as soon as we discover it.
            visited.add((r, c))

            # Add it to the queue to be processed in a future BFS level.
            # IMPORTANT: We do NOT update its distance here.
            q.append([r, c])

        # STEP 1: Find ALL treasure locations.
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    # All treasure cells start at distance 0.
                    q.append([r, c])
                    visited.add((r, c))

        # STEP 2: Start BFS from all treasures simultaneously.
        dist = 0

        # Continue until there are no more cells to explore.
        while q:

            # IMPORTANT:
            # len(q) is evaluated ONCE at the start of this for loop.
            #
            # Therefore, we process ONLY the cells already in the
            # queue at the beginning of this BFS level.
            #
            # Any new neighbors added by addCell() will remain
            # in the queue for the NEXT while iteration.
            for i in range(len(q)):

                # Remove the next cell from the FRONT of the queue.
                r, c = q.popleft()

                # All cells processed in this iteration have
                # the SAME shortest distance to a treasure.
                #
                # First iteration:  treasures -> dist = 0
                # Second iteration: adjacent rooms -> dist = 1
                # Third iteration:  next rooms -> dist = 2
                # And so on...
                grid[r][c] = dist

                # Discover the four adjacent cells.
                #
                # Valid, unvisited neighbors are added to the queue.
                # They will be processed at the NEXT distance level.
                addCell(r + 1, c)  # Down
                addCell(r - 1, c)  # Up
                addCell(r, c + 1)  # Right
                addCell(r, c - 1)  # Left

            # We finished processing EVERY cell at this distance.
            # Increase distance before processing the next level.
            dist += 1