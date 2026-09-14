class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We need to go from top-right to bott-left on a (MxN) grid
        # Can only move right or down, must return count of unique paths
        # For each position we are at we have 2 choices on where to move
        # We will cache each result ata each position on DFS
        # the result is the rest at down adn eight postion from current position
            # Since each position caches the num of wasy to reach end
        # We will start from bootom to start position (bottom-up apporach DP)
        # Last row all ones, other rows not, they are based on sum of down and right cache value

        # Bottom-row Cache
        row = [1] * n

        # Iterate over all rows
        for i in range(m-1):
            newRow = [1] * n
            # Edge case out of bounds (skip right most col, since its always 1)
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            # Update cache row
            row = newRow
        
        return row[0]