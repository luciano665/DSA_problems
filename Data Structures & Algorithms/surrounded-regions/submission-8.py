class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # We need traverse grid and replace a surrounded regiosn og 'O' with X
        # If 'O' is and edge we cant replace it with X we leave it as it is
        # However, a regio of connected 'O' IF surrounded we do replace them with X
        # We can use DFS to traverse borders
        # We know that the traversal over the borders will mark invalid surrounded areas and O to#


        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if (r == rows or c == cols or r < 0 or c < 0 or board[r][c] != 'O'):
                return
            

            # Mark the border as #
            board[r][c] = "#"

            # Recurisve calls to adjecent cells
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        

        # Traverse the border in order to mark border '0' as #
        
        # Column traversal
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c) # This first row (top level) goes to the right from left
            if board[rows-1][c] == 'O':
                dfs(rows-1, c) # This is last row (bottom level) goes to the right from left

        
        # Row traversal
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0) # left top corner and goes down
            if board[r][cols-1] == 'O':
                dfs(r, cols-1) # top right corner and goes down
        

        # We need to traverse one last time over complete board
        for r in range(rows):
            for c in range(cols):
                # Check for # and also 'O'
                # mark: #->O and O->X
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
            