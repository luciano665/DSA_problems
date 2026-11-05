class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # We need to traverse grid using BFS
        # Since at each level (1 minute) 
        # Rotten fruitds (2) all adjacent cells become 2 iff they ar 1
            # If cell is 0 we do no nothing and continue
        # We must keep track of fresh fruits and as well as the time
        # We return the time iff fresh count = 0 since if not -1
            # Since condition is to have 0 fresh fruits if imposible we return -1
        
        # We need to add each rotten fruit cell coord into queue for later traversal


        # Init global vars
        q = collections.deque()
        fresh = 0
        time = 0

        # Iteration to pupulate queue as well as count of fresh fruits
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                # Check 2 things if is fresh or rotten
                if grid[row][col] == 1:
                    # Found a fresh fruit
                    fresh += 1
                if grid[row][col] == 2:
                    # Add rotten fruit to queue
                    q.append((row, col))
        
        # Now we can star the BFS using the queue but we need adj direction in order to move
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Start BFS 
        while fresh > 0 and q:
            length = len(q)
            # Go over current queue
            # each level is a full loop from queue
            for i in range(length):
                r, c = q.popleft()

                # We need to move in adjecent directions
                for dr, dc in directions:
                    row = r +dr
                    col = c + dc

                    # Check if we have adjecent fruit fresh to convert and append direction
                    # we append to queue since we have new rotten fruit to look for its adj cells
                        # Such that we convert a fresh adj to rotten 
                    if (row in range(len(grid)) and col in range(len(grid[0])) and 
                        grid[row][col] == 1):
                        
                        # set the fresh fruit adj to rotten to rott
                        grid[row][col] = 2
                        
                        # Add new rotten to queue for next level traversal
                        q.append((row, col))

                        # upadate count of fresh fruit 
                        fresh -= 1
            # Update level count
            time += 1 
        
        return time if fresh == 0 else  -1




     



        

