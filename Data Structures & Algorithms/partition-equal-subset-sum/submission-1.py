class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Need to return true if 2 subset of nums its sum is equal
            # Otherwise we return False
        
        # We will store each possible sum in set, traversing backwward on nums
        # We update the set of sums on each possible num in nums
            # The new val added if not in set plus all prev traversed vals as new sum
        # If the set contains the target sum we retrun true if not False
        # Also we get the target sum by sumin all elments o nums and divided/2

        # Base case odd sum//2
        if (sum(nums) % 2 != 0):
            return False
        
        # Dp set
        dp = set()
        dp.add(0)
        # Get sum target
        target = sum(nums) // 2

        # Iterate over nums in reverse
        for i in range(len(nums) -1, -1, -1):
            nextDp = set()
            # Go over set val sum 
            for t in dp:
                # Add sum to temp set and also dp val t
                nextDp.add(t + nums[i])
                nextDp.add(t)
            # update dp
            dp = nextDp
        return True if target in dp else False

        