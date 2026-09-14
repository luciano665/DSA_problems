class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        # We need a var to store current max profit
            # If profit combinations <= 0 -> return 0
        # Pick a day to buy and anotehr diff to sell
        # buy must be the min val and sell the max
        # Prices are in oreder according to days ->

        # We will solve this using two pointers 
        # L and R pointer init to -> L=0 and R=1 to point to first indexes of list
        # One var to store current max profit
        # Loop over list while the R pointer is < lentght of list
        # Check if current L is < R if so compute profit and get max of past max profit and current computed profit
        # Else we put the L = R and outsite if/else update R pointer
        # The R pointer must be updated each time to check all possibel vals

        # Init vars/pointers
        maxP = 0 
        l = 0
        r = 1

        # Loop
        while r < len(prices):

            # Check condition to calculate the profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            else:
                l = r
            
            # Update R pointer to check next price day
            r += 1
        
        # Return maxP
        return maxP
        


        