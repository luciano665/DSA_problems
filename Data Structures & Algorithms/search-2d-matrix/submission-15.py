class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bot = ROWS-1

        # 1st Bin-S to find the row where the target may be
        while top <= bot:

            row = (top + bot) // 2

            # Check if target > max-elm at current row
            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bot = row - 1

            else:
                break

        # We must check if the target is in valid row
        if not(top <= bot):
            return False

        # We start the secodn bin-search
        row = (top + bot) // 2

        l = 0
        r = COLS-1

        while l <= r:
            m = (l+r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m -1

            else:
                return True

        # target not in matrix
        return False
        


