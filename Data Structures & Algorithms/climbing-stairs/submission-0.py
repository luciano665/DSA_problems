class Solution:
    def climbStairs(self, n: int) -> int:
        
        # We will use DP with an array of n-elemnets using a cache suct that dont have to keep the tree growing
        # At each current step we are at we need to cache result such that we dont run it again if we found same subproblem
        # Wew will solve each subproblem only once -> O(n)
            # We are caching the result - > AKA Memoization
        # Will start at the bottomp at teh base case ans work way up (bottom up)
        # We start at n and add the possible way to reach n ans tsore it index n in array
        # Then we do the same for the n-1 position
        # For n-2 we add up n + n-1 and store it at n-2 index and so un until the index 0 will be teh result
        # We need to have only 2 vars since the result depends on 2 vars to compute next val
        # Each one being shifted n-1 times

        one, two = 1, 1 # One way to reach n from n-1 and from n positions

        # We traverse n-1 times since the one and two are for n-1 and n posotions
        for i in range(n-1):

            # We need to save curr one val to update two after
            temp = one
            # Adding prev 2 vals to one since one will store the final result
            one = one + two
            two = temp

        return one








