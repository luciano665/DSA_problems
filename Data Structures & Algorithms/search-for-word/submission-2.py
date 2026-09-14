class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # The only way to solve this is by bruteForce: recursive backtrack
        # Need to visit only the vertically and horizontally to form the word from a given cell
        # Must check if word is possible by meeting the codition from above
        # Will use DFS recurively to traverse the grid
        # Also we can revisit a cell on current path
            # Will visit each position (r, c) on board until we found the word

        rows, cols = len(board), len(board[0])
        path = set() # add curr val on our board to no revisit

        # i is current chars we looked at from word
        def dfs(r, c, i):

            # Base case: Get the word
            if i == len(word):
                return True

            # Base case: out of bounds or invalid word
            if (r<0 or c<0 or r>=rows or c>=cols or
                word[i] != board[r][c] or (r,c) in path):
                return False

            # Add r,c into path
            path.add((r, c))

            # Reursive calls on adjecent from current word
            # Need to find word one single time so just one need to be True
                # Of the recursive calls
            res = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1))

            # Need to clean current (r, c) since we no longer visit that position
            path.remove((r, c))
            return res
            
        # Start traversing each pos on board (every starting position)
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): # if found word in board will return True
                    return True
        # Else word not in board (dfs never returns True)
        return False



