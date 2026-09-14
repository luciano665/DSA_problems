class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Must find the min amount of coins to get target
        # Brute force solution: some kinf of DFS/backtrack approach
        # Will use DP-Bottop-Up aproach 
        # Starting at 0 as target and go up until target
        
        # DP array 
        dp = [amount + 1] * (amount + 1)

        # Base case DP[0]
        dp[0] = 0 # takes 0 for 0 val

        # Iteration form 1 to amount+1
        for a in range(1, amount+1):
            # Go over coins
            for c in coins:
                # If reminder is valid ->cont search
                if a - c >= 0:
                    dp[a] = min(dp[a] , 1 + dp[a-c]) # the 1+ is needed sice 1 coin + dp[a-c]
        return dp[amount] if dp[amount] != amount + 1 else -1

