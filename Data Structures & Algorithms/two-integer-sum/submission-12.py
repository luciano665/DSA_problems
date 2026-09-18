class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # We wil use hashmap to store key value pairs
        # Need to iter over nums ans tore index in nums ans the curre val
        # By findin diff of num ans taget in hasmap
        hashM = {}

        for i, n in enumerate(nums):

            diff = target - n

            # Check if the diff is in hashmap 
            if diff in hashM:

                # Since i is curetn index from iteration asn if diff is key value
                # The the lowest index will be the one stored already
                return [hashM[diff], i]

            # Store current num as the key and the index in array as the val
            hashM[n] = i
