class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # We can use DFS to allok first on the borders of the board
        # If boarder is '0' we run dfs on that cell and mark that cell to T
        # Since a valid 4-group of o's must be surrounded only by 'X's 
        # Therefore, if there valid 0's from 0's at border those must be amrked as T
        # After all DFS is done we traverse board again
        # If current cell == T put it bakc ot 0 and if == 0 put to o X

        rows, cols = len(board), len(board[0])

        def dfs(r, c):

            # Check if currenr cell is valid
            if (r < 0 or c < 0 or c == cols or r == rows or board[r][c] != "O"):
                return
            
            # Marked as T (invalid cell for convertion)
            board[r][c] = "T"
            # Recursive calls to adjecent cells from curr cell
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r , c + 1)
            dfs(r, c - 1)

        # Traversal by sides (left-right) with rows
        for r in range(rows):
            # Left Side
            if board[r][0] == "O":
                dfs(r, 0)
            # Right side
            if board[r][cols-1] == "O":
                dfs(r, cols-1)
        
        # Treaversal by sides (upper-lower) with cols
        for c in range(cols):
            # Uppder side
            if board[0][c] == "O":
                dfs(0, c)
            # Lower side
            if board[rows-1][c] == "O":
                dfs(rows-1, c)

        # We will have the invalid 0's as T and valid to convertion as 0
        # Set T's to 0's and 0's as X's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        