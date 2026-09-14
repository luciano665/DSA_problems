class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Use a hashmap

        hashM = {}

        for i, n in enumerate(nums):
            diff = target - n
            # Look if diff is in hasMap
            if diff in hashM:
                return [hashM[diff], i]
            # else we store k-v to hash
            hashM[n] = i
        
        return 

