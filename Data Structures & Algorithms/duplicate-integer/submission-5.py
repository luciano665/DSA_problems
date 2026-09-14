class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Will use a hashMap

        hashS = {}

        for i in range(len(nums)):

            hashS[nums[i]] = 1 + hashS.get(nums[i], 0)

            if hashS[nums[i]] >= 2:
                return True

        return False