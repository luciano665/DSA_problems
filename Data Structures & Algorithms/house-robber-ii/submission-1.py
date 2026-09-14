class Solution:
    def rob(self, nums: List[int]) -> int:
        # The last value is adjacent to the first value on nums
            # If we rob one of them we can rob the other one
        # We can rob adjacnet houses
        # We need to maximize the amount of houses we can rob
        # We will reuse the solution from house-robber-1 but changed
        # We will rob from entire array as subarrays
            # except the first value
            # Except the last value
            # If the nums only have one house
        # So we need to run the helper func on the subarrays
        
        # Call to helper function to riobn houses 
        # On different subarrays from nums array
            # If nums-len=1, excluding nums[0] and exluding last element
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

        


    # Helper function from house-robber-1
    def helper(self, nums):
        # Adjacent houses
        rob1, rob2 = 0, 0 # Store max amount to rob from prev 2 houses
        
        # Iterate over nums
        for num in nums:
            # Get curr max on subarray
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        
        return rob2