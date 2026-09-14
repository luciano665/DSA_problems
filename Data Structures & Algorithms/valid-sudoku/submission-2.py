class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #HASHMAP key is column number and value is another set
        #All values in teh colums 
        #same for rows
        cols = collections.defaultdict(set)
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                #If current sqaure is empty we skip it
                if board[r][c] == ".":
                    continue
                #If not empty
                #If Current number we are at is inside current row or col or current square
                #It is a duplicate
                if (board[r][c] in row[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3 , c//3]):
                    return False
                #If not detected update hashmap
                cols[c].add(board[r][c])
                row[r].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])

        return True