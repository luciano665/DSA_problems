class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Find the min cost to get to the top of floor (len(cost) + 1)
        # We can start from index 0 or 1 and the cost is the cost[i]
        # From cost[i] cna you decide to climb one(i+1) or two(i+2) indexes
        # We will use DP to cache each min cost to reach top floor from each index
        # We will have n subproblem since n is len of cost list
        # We will use each time 2 single vars of the cost list
        # Will start at end of cost list to cache each cost
        # At the end each index in cost will have the value to reach the tops of the stairs
            # From that current index, we will retunr the min(cost[0], cost[1])
        
        # Update input array to add top of stairs
        cost.append(0)

        # Iterate over array in revere from last-pos-3 (since -1 is last post 0-index)
        for i in range(len(cost)-3, -1, -1):
            # Store at each index from the (last stair cost)-1  up to 0 zero index
                # The cost to reach the top of the stairs
            cost[i] = min(cost[i] + cost[i+1], cost[i]+cost[i+2]) # Single jump, double jump

        # Since we can can star from index 0 or 1 -> need to take min of both
        return min(cost[0], cost[1])
        


        

