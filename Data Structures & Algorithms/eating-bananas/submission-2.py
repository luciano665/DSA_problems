class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Since we have to eat all piles at a k-rate within h hours
        # Upper bound of k is the largest pile
        # Lower bound of k is 1
        # That will be our array to bin-search to find the min k <= h
        # h is alwasy greater than or equal to the lenght

        l = 1
        r = max(piles)
        # Current result is max in piles
        res = r

        while l <= r:
            k = (l+r) // 2

            totalTime = 0 
            for p in piles:
                # With current k we look for how much it takes to eat all piles
                totalTime += math.ceil(float(p)/k)

                # We find a canditate solution
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                    l = k + 1
        return res





