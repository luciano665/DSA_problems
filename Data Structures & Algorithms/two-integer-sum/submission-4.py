class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Will use a hashmap for: {val: index}
        final = {}

        # Iterate over nums enumerated (i, n), i=index, n=num
        for i, n in enumerate(nums): # (0: nums[0], 1....)
            # Get difference
            diff = target - n

            if diff in final:
                return [final[diff], i]

            # Update hasmap if not
            final[n] = i








        