class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # We want the max amount of houses
        # We cant rob houses that are adjacent to each other (neighbors)
        # Always start with decision tree
            # Draw all subproblems
        # We rob one house and have a subproblem on the subarray
        # We need to find the max house to rob on that subproblem 
        # Teh otehr option is not robbing that house and instead we skip that first house entirely
        # We only need to mantain the 2 rob houses alll the time

        rob1, rob2 = 0, 0
        
        # Iterate over nums
        for n in nums:
            # [rob1, rob2, n, n+1, ..]
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2