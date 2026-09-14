class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Will use a hashmap for: {val: index}
        final = {}

        # Iterate over nums enumerated (i, n), i=index, n=num
        for i, n in enumerate(nums): # (0: nums[0], 1....)
            # Get difference
            diff = target - n

            if diff in final:
                # If it is stored we return hashmap[diff] (index of value already stored) 
                #and i current index of the nums list were are iterating over
                return [final[diff], i]

            # Update hasmap if not
            final[n] = i








        