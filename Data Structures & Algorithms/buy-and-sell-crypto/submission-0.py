class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        # We need a var to store current max profit
            # If profit combinations <= 0 -> return 0
        # Pick a day to buy and anotehr diff to sell
        # buy must be the min val and sell the max


        # Init vars to store max profit at set min-buy as first element
        maxP = 0
        minB = prices[0]

        # Loop over the prices list
        for sell in prices:

            # Get current max profit of the current max profit and the possibel new max profit
            maxP = max(maxP, sell - minB)
            # Update min buy to stay as it if is < than the curren sell
            minB = min(minB, sell)
        
        # Outside loop return max profit
        return maxP
        


        