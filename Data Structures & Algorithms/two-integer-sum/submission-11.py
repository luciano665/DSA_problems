class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # We wil use hashmap to store key value pairs
        # Need to iter over nums ans tore index in nums ans the curre val
        # By findin diff of num ans taget in hasmap
        hashM = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in hashM:
                return [hashM[diff], i]

            # Store current index asn um into hash
            hashM[n] = i
            