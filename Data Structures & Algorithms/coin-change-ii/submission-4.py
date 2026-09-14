class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # We will use 2D grid for a cache DP solution
        # Where the rows are the coins we have 
        # And the cols are the range of vals from 0 to amount
        # Must return all possible combinations of coins that add up to the amount target
        # DP bottom-up approach
        # For psace optminiazaton we will fgto from last cell bootm to the right cle on each row
        #

        # Init dp cache
        # Rows are #-coins and cols amount rengre form 0
        dp = [[0] * (len(coins) + 1) for i in range(amount+1)]
        # Init dp[0] to be 1 (ways tp get 0, only one way possible)
        # For each row
        dp[0] = [1] * (len(coins) + 1)

        # iterate over amounts + 1 from 1
        for a in range(1, amount + 1):

            # Iterate over 2D grid (bottom up)
            for i in range(len(coins) -1, -1, -1):
            
                # Set current cell in grid
                # i=coins avaliable, a=current target sum
                # First decision skip coint at index-i
                dp[a][i] = dp[a][i+1]

                # second decision
                # We have a prev val to add to current cell from 
                # cell at current a-coins[i]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a-coins[i]][i]
        
        # Since bottom-up, result is at (a, 0)
        return dp[amount][0]

