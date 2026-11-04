class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # We have a 2D matrix where there are 3 diff values
        # -1 can traverse this cell, 0 treasure and INF which can traverse
        # On each INF eciunter we must upadte the INF to the shortes dist from it
            # to the chest
        # We need to use BFS but in a smart way, multi-source BFS
        # Where we start BFS from the chest location
        # Such that at each level the distance = level wea re from each chest
        # All cells that are 0 go into a queue then process level by level
        # For each cell we must marked as visitided and store current level as dist
        # We add adjecent cells (0's) iff have been not visited before

        # Get the len of rows and cols
        rows = len(grid)
        cols = len(grid[0])
        # queue to store the 0 coords form grid to explore
        q = deque()
        # set to store visited coords
        visited = set()

        def addCell(r, c):

            # base case 
            if ( min(r, c) < 0 or r == rows or c == cols or (r, c) in visited 
                or grid[r][c] == -1):

                return
            
            # Need to append into queue and upadte set of current coords
            # Of INF locations
            visited.add((r, c))
            q.append([r, c])


        # start travesal of grid to populate the queue of chest locations only
        for r in range(rows):
            for c in range(cols):

                # Must start BFS if we encounter 0 
                if grid[r][c] == 0:
                    # Add current visited chest location into queue for BFS later
                    q.append([r, c])
                    visited.add((r, c))

        # Keep track distance
        dist = 0

        # At this point we have the queue populated with only chest locations
        # Need to do BFS from this locations and upadte grid 
        while q:
            # go over queue 
            for i in range(len(q)):
                r, c = q.popleft()
                # update grid at r, c to the current shortest distance
                grid[r][c] = dist

                # Visit all adjecent location from current 
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            # Update dist + 1
            dist += 1



        

        

