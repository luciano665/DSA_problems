class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # We will use a Bin-search approach 
        # We now each row is sorted (->) as well as rows below are greater that rows above
        # We will need to do 2 separate bin-search
        # To look for the row and then bin in the row
        
        
        ROWS, COLS = len(matrix), len(matrix[0])

        # Two pinter top and bottom (top is the last )
        top = 0
        bott = ROWS - 1

        # Start the Bin-search
        while top <= bott:
            row = (top + bott) // 2

            # If max elemnt in row is less than target shrink up
            if target > matrix[row][-1]:
                top = row + 1
            
            # If smallest elment in row is greater than target shrink down
            elif target < matrix[row][0]:
                bott = row - 1
            
            # Else break we found valid row
            else:
                break

        # Must check of we have target is in a valid row 
        if not(top <= bott):
            return False
        
        # Get row 
        row = (top + bott) // 2
        # Now we perform the second bin-serch on the rows
        l = 0
        r = COLS - 1

        while l <= r:
            m = (l+r) // 2

            # Check if mid in row < target
            if target > matrix[row][m]:
                l = m + 1

            elif target < matrix[row][m]:
                r = m - 1

            else:
                return True
        
        # Target not in matrix
        return False
        


