class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We will use sliding window approach
        # Where at idx i is the current sell price and on the left is buy price
        # If profit is never > 0 we set profit to 0 return 0
        # Keep track of profit is value is > 0
        # Profit = sell - buy


        currMax = 0
        # Wwe will use 2 pointers, one is buy and other is sell
        l = 0
        r = 1

        # go over list while the most right pointer up to end of list
        while r < len(prices):

            # Check if we have valid profit to get (if > 0)
            # This is true o iff buy price is less than sell price
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                currMax = max(currMax, profit)
            else:
                # Since buy price > sell price (no profit to gain)
                # We try do buy at current sell price
                l = r
            
            # Update r pointer to check next sell price
            r += 1
        
        return currMax


           
            




