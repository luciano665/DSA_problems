class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Will use a prefix and post fix apporahc such that we first computre the prefix
        # Will do this in the same output array init to all 1s len of nums

        # We will first compute the prefix product of all nums before the i-th number

        res = [1] * (len(nums))

        # Init prefix  to 1 since element 0 in nums has not prefix
        preFix = 1

        # It 
        for i in range(len(nums)):

            # compute prefix of i-th element and store at res
            res[i] *= preFix
            # Update prefix to be i-element in nums
            preFix *= nums[i]

        # We do postfix from right to left on nums

        postFix = 1
        for j in range(len(nums)-1, -1, -1):

            # Compute the postfix of the i-th element
            res[j] *= postFix
            # Update postFix to be the next post (right of) current i-th in nums
            postFix *= nums[j]

        return res
            
