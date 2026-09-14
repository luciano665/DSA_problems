class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Will use backtracking to find al possible subsets of nums
        # We have 2^n num of subsets where n is the len of nums
        # The problem is not efficient to solve
        # Will use dfs to build the decision tree
        # At each level we decide to include or not include the nums[i]
        # First 2-decisions are made from first element on nums


        # Array empty to store subsets
        res = []
        # Array for current subset
        subset = []

        def dfs(i):

            # Base case if current i is out of bounds
            # We are past of leaf node
            if i >= len(nums):
                res.append(subset.copy()) # subset is going the modified
                return 
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1) # Like left branch of deci tree

            # Decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        # call dfs from nums[0] and return res list of lists
        dfs(0)
        return res
        

