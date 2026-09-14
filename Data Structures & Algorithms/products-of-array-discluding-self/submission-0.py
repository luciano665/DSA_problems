class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Init array with ones and with lenght of inputs
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #First update element of the list to return 
            prefix *= nums[i]  #-> update of prefix with value in nums
        postfix = 1

        #Start at the end of input array and go until the beginning of it
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix # this is basically multiplying prefix and postfix
            postfix *= nums[i] # update of post fix
        return res

