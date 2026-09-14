class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # Need to form all possible subsets from nums
        # Nums can have duplicates but subsets can contain duplicate subsets
        # For each input on nums we have a choice to include it or not
        # Will backtrack using apointer at index 0
            # However, we need to see we dont get dplicate subsets
        # To avoid this duplcates we need to ensure that only one path include repated 
            # values from nums
            # We accomplish this by moving pointer if i == i+1
        # For this we need to sort the array
        
        # Store all subsets here
        res = []
        nums.sort()
        
        def backtrack(i, subset):

            if i == len(nums):
                res.append(subset[::]) # Create a copy with [::] or .copy()
                return
            
            # Decision 1: All subsets that include nums[i]
            subset.append(nums[i])
            # Recursion step for next one
            backtrack(i + 1, subset)
            # For next decision remove value we just added
            subset.pop()

            # Decision 2: All subsets that do not include nums[i]
            # If duplicate found we skip it -> this adds the epmty array into subset
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i+1
            
            # Subset with -1 val we just pop before (we do not include that val)
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
