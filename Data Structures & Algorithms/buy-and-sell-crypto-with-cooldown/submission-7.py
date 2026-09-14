class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Must return the maxprofit 
        # If we sell or buy we must cooldown a day
        # Will use a cache using hashmap to store the if sell/buy adn given day i

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):

            # Base case out of bounds
            if i >= len(prices):
                return 0
            
            # Base casealredy computed 
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            # Cases if we buy or if we sell
            if buying:
                # Recursive call to buy: curMaxPro - price[i]
                buy = dfs(i + 1, not buying) - prices[i]
                # caching
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # Recursive call: currMaxPro + price[i]
                sell = dfs(i + 2, not buying) + prices[i]
                # caching
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)