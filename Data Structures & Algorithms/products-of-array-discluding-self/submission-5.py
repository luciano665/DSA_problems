class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We will use prefix and psit fix sum approach optimal 
        # In a single array of extra use
        # Prefix will be all on th eleft first pass
        # Postfix all formr to left second pass
        # We init a new array of results of len nums with 1

        res = [1] * len(nums)

        # Since no element on left of first num (multiply by 1)
        prefix = 1
        # Here it computes from l to r 
        for i in range(len(nums)):
            # Update prefix product of elemnts on the left of nums[i]
            res[i] = prefix
            # Update prefix (prduct of elemnts on the left times new num on the L)
            # To put into the res[i] as the prefix product of itmes on left 
            # Each time you udpate prefix:is the product of elemnts of next num[i]
                # on the left   
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res