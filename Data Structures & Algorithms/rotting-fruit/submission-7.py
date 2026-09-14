class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Will to start from a rotten fruit (2) (need to get positions)
        # We will need BFS to search level by level since the min to taken all fres into rotten is the last level
        # Need to count all fresh foods and get all 2's coord in grid
        # After that we perform BFS from each 2's cells in queue
        # Check if current r,c in grid are valid

        queue = deque()
        fresh = 0
        time = 0

        # 1st traversl to get 2(r,c) and fresh counts
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        # We have the coord of the the 2's in grid
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Start 2nd travesal
        while fresh > 0 and queue:
            # Get curr lenght of queue
            lenght = len(queue)
            # Get adjecents of current r,c in grid
            for i in range(lenght):
                r, c = queue.popleft()
                for dr, dc in directions:
                    # Update new r, c 
                    row, col = r + dr, c + dc
                    # Check if new r and c are valid to be considered
                    # are a fruit 
                    if (row in range(len(grid)) and col in range(len(grid[0]))
                         and grid[row][col] == 1):
                         # if valid update 1 to 2
                         grid[row][col] = 2
                         queue.append((row, col))
                         fresh -=1
            # Update time after adjcents on current level traversal
            time += 1

        return time if fresh == 0 else -1

                